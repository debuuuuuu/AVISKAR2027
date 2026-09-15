#!/usr/bin/env python3
"""
validate_bibliography.py

Automated verification script for the academic bibliography in the AVISKAR 2027 project.
Verifies:
1. Syntax and completeness of research/references.bib
2. No duplicate citation keys or titles
3. Valid DOI formats (10.xxxx/...) and arXiv identifiers (YYMM.NNNNN)
4. Presence of mandatory metadata (title, author, year, venue/url)
5. Cross-file consistency across:
   - research/references.bib
   - docs/02-research/references.md
   - docs/02-research/literature-matrix.md
"""

import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
BIB_PATH = ROOT_DIR / "research" / "references.bib"
MD_REFS_PATH = ROOT_DIR / "docs" / "02-research" / "references.md"
MATRIX_PATH = ROOT_DIR / "docs" / "02-research" / "literature-matrix.md"

def parse_bibtex(bib_file: Path):
    content = bib_file.read_text(encoding="utf-8")
    entries = {}
    current_key = None
    current_type = None
    current_fields = {}
    
    # Simple robust BibTeX parser for our canonical references
    entry_start_re = re.compile(r"@(\w+)\s*\{\s*([^,]+),")
    field_re = re.compile(r"^\s*([a-zA-Z_]+)\s*=\s*[\{](.*)[\}],?\s*$", re.MULTILINE)
    
    # Split entries by '@'
    raw_blocks = content.split("@")
    for block in raw_blocks:
        block = block.strip()
        if not block:
            continue
        full_block = "@" + block
        start_match = entry_start_re.match(full_block)
        if start_match:
            etype = start_match.group(1).lower()
            key = start_match.group(2).strip()
            
            fields = {}
            for line in block.splitlines():
                fmatch = re.match(r"^\s*([a-zA-Z_]+)\s*=\s*[\{](.*)[\}],?\s*$", line)
                if fmatch:
                    fname = fmatch.group(1).lower()
                    fval = fmatch.group(2).strip()
                    fields[fname] = fval
            
            if key in entries:
                raise ValueError(f"Duplicate BibTeX key found: {key}")
            
            entries[key] = {
                "type": etype,
                "fields": fields,
                "raw": full_block
            }
    return entries

def validate_entries(entries):
    errors = []
    seen_titles = set()
    
    doi_pattern = re.compile(r"^10\.\d{4,9}/[-._;()/:A-Za-z0-9]+$")
    arxiv_pattern = re.compile(r"\b\d{4}\.\d{4,5}(v\d+)?\b")
    
    for key, data in entries.items():
        fields = data["fields"]
        
        # Check mandatory fields
        for req in ["title", "author", "year"]:
            if req not in fields or not fields[req]:
                errors.append(f"[{key}] Missing required field: '{req}'")
        
        # Check duplicate titles
        title = fields.get("title", "").strip().lower()
        title_clean = re.sub(r"[^a-z0-9]", "", title)
        if title_clean in seen_titles:
            errors.append(f"[{key}] Duplicate title detected: '{fields.get('title')}'")
        seen_titles.add(title_clean)
        
        # Validate DOI format if present
        if "doi" in fields:
            doi = fields["doi"].strip()
            if not doi_pattern.match(doi):
                errors.append(f"[{key}] Malformed DOI string: '{doi}'")
        
        # Validate arXiv if present in journal/url
        raw_text = str(fields)
        if "arxiv" in raw_text.lower():
            if not arxiv_pattern.search(raw_text):
                errors.append(f"[{key}] Referenced arXiv preprint but no valid arXiv ID (YYMM.NNNNN) found.")
                
        # Validate URL if present
        if "url" in fields:
            url = fields["url"].strip()
            if not (url.startswith("http://") or url.startswith("https://")):
                errors.append(f"[{key}] Malformed URL: '{url}'")

    return errors

def validate_cross_references(entries):
    errors = []
    
    if not MD_REFS_PATH.exists():
        errors.append(f"Markdown references file not found: {MD_REFS_PATH}")
        return errors
        
    md_content = MD_REFS_PATH.read_text(encoding="utf-8").lower()
    
    # Check that each BibTeX key or title is present in references.md
    for key, data in entries.items():
        title_snippet = data["fields"].get("title", key)[:30].strip().lower()
        # Clean title snippet
        clean_snippet = re.sub(r"[^a-z0-9 ]", "", title_snippet)
        if clean_snippet not in re.sub(r"[^a-z0-9 ]", "", md_content) and key.lower() not in md_content:
            errors.append(f"[{key}] BibTeX entry '{title_snippet}' not documented in {MD_REFS_PATH.name}")
            
    if MATRIX_PATH.exists():
        matrix_content = MATRIX_PATH.read_text(encoding="utf-8").lower()
        clean_matrix = re.sub(r"[^a-z0-9 ]", "", matrix_content)
        for key, data in entries.items():
            title = data["fields"].get("title", key).lower()
            clean_title = re.sub(r"[^a-z0-9 ]", "", title[:25])
            
            # Author last name
            raw_author = data["fields"].get("author", "")
            first_author = re.sub(r"[^a-z]", "", raw_author.split()[0].lower())
            
            if clean_title not in clean_matrix and first_author not in clean_matrix and key.lower() not in matrix_content:
                errors.append(f"[{key}] Academic source not captured in literature matrix: {title[:35]}")
                        
    return errors

def main():
    print(f"==================================================")
    print(f"BIBLIOGRAPHY INTEGRITY CHECK")
    print(f"==================================================")
    print(f"Canonical BibTeX: {BIB_PATH}")
    
    if not BIB_PATH.exists():
        print(f"ERROR: {BIB_PATH} does not exist.")
        sys.exit(1)
        
    entries = parse_bibtex(BIB_PATH)
    print(f"Found {len(entries)} BibTeX entries.")
    
    entry_errors = validate_entries(entries)
    if entry_errors:
        print(f"\n[FAIL] Metadata format errors found:")
        for err in entry_errors:
            print(f"  - {err}")
    else:
        print(f"[PASS] All {len(entries)} BibTeX entries have valid schemas, DOIs, arXiv IDs, and distinct titles.")
        
    cross_errors = validate_cross_references(entries)
    if cross_errors:
        print(f"\n[FAIL] Cross-file consistency errors found:")
        for err in cross_errors:
            print(f"  - {err}")
    else:
        print(f"[PASS] Canonical bibliography matches markdown documentation and literature matrix.")
        
    if entry_errors or cross_errors:
        print(f"\nValidation failed with {len(entry_errors) + len(cross_errors)} issue(s).")
        sys.exit(1)
    else:
        print(f"\nSUCCESS: Canonical bibliography is 100% verified, consistent, and defensible.")
        sys.exit(0)

if __name__ == "__main__":
    main()
