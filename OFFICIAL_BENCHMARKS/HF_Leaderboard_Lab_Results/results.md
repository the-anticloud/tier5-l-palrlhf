# HF_Leaderboard_Lab_Results

**Project:** `L_PALRLHF`  
**Tier:** `TIER_5_WORLD_NEURO_EMBODIED`  
**Slug:** `huggingface/trl`  
**Commit:** `48f7f0f0a3dc`  
**Run:** `2026-09-30T15:07:07.146295+00:00`  

## Isolation Environment

| Field | Value |
| ----- | ----- |
| Platform | `win32` |
| Python | `3.12.10` |
| HF model | `distilbert-base-uncased` |
| HF load time | `4.42s` |
| Inference device | `cpu` |

## Results

**Framework:** [HuggingFace Open LLM Leaderboard (proxy via distilbert-base-uncased)](https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive)

**Model used:** `distilbert-base-uncased`

### Inference Latency (Classification)

| Metric | Value |
| ------ | ----- |
| Avg latency | **45.32 ms** |
| Min latency | 39.49 ms |
| Max latency | 49.56 ms |
| Samples | 5 |

### Real Tokenization Results

| Field | Value |
| ----- | ----- |
| Token count | **40** |
| Tokenization latency | 1.0 ms |
| Classification label | `LABEL_0` |
| Classification score | 0.5888 |
| Classification latency | 81.47 ms |
| Status | **PASS** |

**Input text tokenized:**
```
L_PALRLHF (huggingface/trl) — 552 files, 117528 source lines, licence Apache-2.0, primary language ['Python']
```

**First 20 tokens:**
```
['[CLS]', 'l', '_', 'pal', '##rl', '##h', '##f', '(', 'hugging', '##face', '/', 'tr', '##l', ')', '—', '55', '##2', 'files', ',', '117']
```

> Full MMLU/HellaSwag/TruthfulQA/ARC/Winogrande/GSM8K require dedicated GPU.
> These results are CPU inference proxy metrics using distilbert-base-uncased.

---
_Anticloud Benchmark Suite — isolation log — 2026-09-30T15:07:07.146295+00:00_