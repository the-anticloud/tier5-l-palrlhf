# Deploy Guide — L_PALRLHF
**Tier:** TIER_5_WORLD_NEURO_EMBODIED | **Stack:** Python 3.11, PyTorch 2.10+, trl 0.8+, PAX 27B, AIOSS_FORMAT
**Air-gap capable after initial setup.**

## Prerequisites
Python 3.11+, PyTorch 2.10+, trl 0.8+, A100 80GB for training. Process-level annotation data required.

## Environment
A100 80GB for training. T4 for inference evaluation. 128GB RAM.

## AIOSS Integration
```bash
aioss init --module L_PALRLHF --output ./l_palrlhf.aioss
aioss append --chain ./l_palrlhf.aioss --payload ./output.bin --module L_PALRLHF
aioss verify --chain ./l_palrlhf.aioss
```

## Air-Gap Setup
```bash
pip download -r requirements.txt -d ./wheels/
pip install --no-index --find-links ./wheels/ -r requirements.txt
```

## PAX 27B Harness Wiring
```python
from anticloud_pax import PAXHarness
harness = PAXHarness(
    model_path="./pax-27b-q4.gguf",
    module="L_PALRLHF",
    aioss_chain="./L_PALRLHF.aioss",
    classification="L5_NARROW_L2_GENERAL"
)
result = harness.process(input_data)
```

## Verification
```bash
aioss verify --chain ./L_PALRLHF.aioss --verbose
python -m L_PALRLHF.tests.smoke
```
