# Developer Cookbook — L_PALRLHF
**Stack:** Python 3.11, PyTorch 2.10+, trl 0.8+, PAX 27B, AIOSS_FORMAT
**Domain:** PALRLHF: process-aware LRLHF — reward model from process not just outcome for PAX 27B

## Process-aware RLHF training
```python
from l_palrlhf import PALRLHFTrainer

trainer = PALRLHFTrainer(
    model="./pax-27b-fp16.safetensors",
    process_reward_model="./anticloud_prm/",
    outcome_reward_model="./anticloud_orm/",
    process_weight=0.5,  # mix of process and outcome reward
    aioss_chain="./palrlhf.aioss"
)

trainer.train(
    dataset="./anticloud_reasoning_data.jsonl",
    n_steps=3000
)

# Evaluate step-level reasoning quality
eval = trainer.evaluate("./step_quality_bench.jsonl")
print(f"Step accuracy: {eval.step_accuracy:.3f}")
print(f"Final accuracy: {eval.final_accuracy:.3f}")
```

## AIOSS Chain Append
```python
import hashlib, time

def aioss_append(chain_path, payload: bytes, module_id: str):
    entry_hash = hashlib.sha3_256(payload).digest()
    ts = int(time.time_ns()).to_bytes(8, 'big')
    with open(chain_path, 'rb') as f:
        f.seek(-32, 2); prev_hash = f.read(32)
    new_hash = hashlib.sha3_256(prev_hash + entry_hash + ts).digest()
    with open(chain_path, 'ab') as f:
        f.write(ts + entry_hash + new_hash)
    return new_hash.hex()
```
