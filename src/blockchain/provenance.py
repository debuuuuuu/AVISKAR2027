import hashlib
import time
from typing import List, Optional


class MerkleTree:
    """
    Standard cryptographic Merkle Tree for batching evidence records into 32-byte commitments.
    """

    def __init__(self, leaves: List[str]):
        # Ensure all leaves are SHA-256 hashes
        self.leaves = [
            leaf if len(leaf) == 64 and all(c in "0123456789abcdefABCDEF" for c in leaf)
            else hashlib.sha256(leaf.encode("utf-8")).hexdigest()
            for leaf in leaves
        ]
        if not self.leaves:
            self.leaves = [hashlib.sha256(b"empty_tree").hexdigest()]
        self.root = self._build_tree(self.leaves)

    def _build_tree(self, nodes: List[str]) -> str:
        if len(nodes) == 1:
            return nodes[0]

        next_level: List[str] = []
        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = nodes[i + 1] if i + 1 < len(nodes) else left
            combined = left + right
            parent = hashlib.sha256(combined.encode("utf-8")).hexdigest()
            next_level.append(parent)

        return self._build_tree(next_level)

    def get_root(self) -> str:
        return self.root


class BlockchainProvenanceAnchor:
    """
    Manages anchoring of Merkle root commitments to simulated or EVM smart contracts.
    """

    def __init__(self, network_name: str = "simulated_ledger"):
        self.network_name = network_name
        self.anchored_commitments: List[dict] = []

    def commit_batch(self, evidence_hashes: List[str]) -> dict:
        """Computes Merkle root and anchors it."""
        tree = MerkleTree(evidence_hashes)
        root = tree.get_root()
        commitment = {
            "merkle_root": f"0x{root}",
            "record_count": len(evidence_hashes),
            "timestamp": int(time.time()),
            "network": self.network_name,
            "tx_hash": f"0x{hashlib.sha256(f'{root}:{time.time()}'.encode('utf-8')).hexdigest()}"
        }
        self.anchored_commitments.append(commitment)
        return commitment

    def verify_commitment(self, merkle_root: str) -> bool:
        """Verifies whether a commitment root exists in the anchor registry."""
        normalized = merkle_root if merkle_root.startswith("0x") else f"0x{merkle_root}"
        return any(c["merkle_root"] == normalized for c in self.anchored_commitments)
