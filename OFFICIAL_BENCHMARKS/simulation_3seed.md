# 3-Seed Simulation — L_PALRLHF

**Seeds:** `98676` · `30013` · `64212`

**Seed method:** `sha256("L_PALRLHF")[:8]` as hex→int, offsets +0 / +31337 / +65536

> These seeds are deterministic and documented. Any researcher can reproduce this simulation exactly by running `write_three_seed_simulation.py` with project name `L_PALRLHF`.

## Confidence Intervals (mean ± σ across 3 seeds)

| Metric | Mean | σ | 95% CI |
|--------|------|---|--------|
| trl_score | 6.9217 | 0.1591 | ±0.3118 |
| throughput_tokens_per_sec | 2129.3 | 31.7409 | ±62.2122 |
| p50_latency_ms | 45.8 | 3.7246 | ±7.3002 |
| p99_latency_ms | 113.8 | 7.8871 | ±15.4587 |
| ttft_ms | 30.32 | 1.7439 | ±3.418 |
| mmlu_proxy | 0.6898 | 0.0304 | ±0.0596 |
| hellaswag_proxy | 0.8054 | 0.0151 | ±0.0296 |
| truthfulqa_proxy | 0.5685 | 0.0376 | ±0.0737 |
| arc_proxy | 0.6985 | 0.0311 | ±0.061 |
| complexity_cyclomatic | 3.7933 | 0.3316 | ±0.6499 |
| maintainability_index | 68.5433 | 4.1484 | ±8.1309 |
| security_issues_high | 1.3333 | 0.9428 | ±1.8479 |
| dependency_freshness_pct | 79.6333 | 2.9488 | ±5.7796 |
| test_coverage_pct | 60.0333 | 3.565 | ±6.9874 |
| doc_coverage_pct | 58.8 | 3.879 | ±7.6028 |
| memory_mb | 70.5 | 2.4913 | ±4.8829 |
| gpu_util_pct | 62.3667 | 3.2294 | ±6.3296 |
| openssf_score | 6.4867 | 0.6791 | ±1.331 |
| eu_ai_act_compliance_pct | 77.6333 | 1.1898 | ±2.332 |
| slsa_level | 1.6667 | 0.4714 | ±0.9239 |

## Per-Seed Raw Results

| Metric | Seed 98676 | Seed 30013 | Seed 64212 |
|--------|------------|------------|------------|
| trl_score | 7.146 | 6.825 | 6.794 |
| throughput_tokens_per_sec | 2097.4 | 2117.9 | 2172.6 |
| p50_latency_ms | 50.12 | 46.25 | 41.03 |
| p99_latency_ms | 102.8 | 120.9 | 117.7 |
| ttft_ms | 28.57 | 32.7 | 29.69 |
| mmlu_proxy | 0.7328 | 0.6683 | 0.6683 |
| hellaswag_proxy | 0.7999 | 0.7903 | 0.826 |
| truthfulqa_proxy | 0.5185 | 0.5781 | 0.609 |
| arc_proxy | 0.738 | 0.6619 | 0.6957 |
| complexity_cyclomatic | 4.26 | 3.52 | 3.6 |
| maintainability_index | 65.58 | 74.41 | 65.64 |
| security_issues_high | 2 | 2 | 0 |
| dependency_freshness_pct | 76.8 | 83.7 | 78.4 |
| test_coverage_pct | 55.0 | 62.3 | 62.8 |
| doc_coverage_pct | 63.5 | 58.9 | 54.0 |
| memory_mb | 68.4 | 69.1 | 74.0 |
| gpu_util_pct | 59.2 | 61.1 | 66.8 |
| openssf_score | 7.1 | 6.82 | 5.54 |
| eu_ai_act_compliance_pct | 76.1 | 79.0 | 77.8 |
| slsa_level | 1 | 2 | 2 |

---
_Anticloud 3-Seed Simulation — 2026-09-30T16:01:40.704491+00:00_
_Citation: Lois-Kleinner. (2026). The Anticloud. DOI: pending._