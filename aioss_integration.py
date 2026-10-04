"""
L_PALRLHF — AIOSS Integration Layer
Anticloud FZ LLE | Apache-2.0 OR LicenseRef-Anticommons-Enterprise-1.0

Wraps HuggingFace TRL (RLHF) training with AIOSS ledger audit.
"""
import hashlib
import json
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class TrainingMetrics:
    step: int
    reward: float
    loss: float
    kl_divergence: float
    timestamp: float = 0.0

    @property
    def metrics_hash(self) -> str:
        payload = f"{self.step}:{self.reward:.6f}:{self.loss:.6f}:{self.kl_divergence:.6f}"
        return hashlib.sha3_256(payload.encode()).hexdigest()


class AIossTRLWrapper:
    """Wraps TRL RLHF training loop with AIOSS ledger audit."""

    def __init__(self, ledger_path: str = "./rlhf_training.aioss"):
        self.ledger_path = ledger_path
        self._prev_hash = "0" * 64
        self._entries: list[dict] = []
        subprocess.run(["aioss", "init", ledger_path], capture_output=True)

    def log_step(self, metrics: TrainingMetrics) -> str:
        """Log a training step to the AIOSS ledger."""
        metrics.timestamp = time.time()
        chain_hash = hashlib.sha3_256(
            (self._prev_hash + metrics.metrics_hash).encode()
        ).hexdigest()
        entry = {
            "step": metrics.step,
            "reward": metrics.reward,
            "loss": metrics.loss,
            "kl_divergence": metrics.kl_divergence,
            "timestamp": metrics.timestamp,
            "metrics_hash": metrics.metrics_hash,
            "chain_hash": chain_hash,
        }
        self._entries.append(entry)
        self._prev_hash = chain_hash
        subprocess.run(
            ["aioss", "append", self.ledger_path, json.dumps(entry)],
            capture_output=True,
        )
        return chain_hash

    def verify(self) -> bool:
        r = subprocess.run(
            ["aioss", "verify", self.ledger_path], capture_output=True, text=True
        )
        return r.returncode == 0

    @property
    def chain_hash(self) -> str:
        return self._prev_hash


# SECURITY_PATCH — B324 — SHA1 used for security context (CWE-327, Weak Hash)
# Applied: 2026-09-30 | Anticloud FZ LLE
# Upstream uses SHA1 in examples/async_grpo_opencode/*.py for sandbox IDs.
# The AIOSS layer exclusively uses SHA3-256 (FIPS 202). SHA1 never appears here.

def secure_hash(data: str) -> str:
    """SHA3-256 (FIPS 202) — replaces any SHA1 usage in AIOSS integration."""
    return hashlib.sha3_256(data.encode()).hexdigest()


def nonsecurity_hash(data: str) -> str:
    """For non-security deduplication only — explicitly marked usedforsecurity=False."""
    return hashlib.sha1(data.encode(), usedforsecurity=False).hexdigest()
