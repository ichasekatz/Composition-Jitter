# Composition Jittering Utility

This script applies **controlled Gaussian jitter** to multicomponent alloy compositions stored in a CSV file.  
It is designed to generate **nearby compositions** around existing points while preserving physical constraints.

---

## Purpose

The script perturbs existing 5-component compositions to:

- Introduce small, realistic compositional noise
- Maintain **non-negativity**
- Enforce **exact normalization** (each composition sums to 1)
- Generate a new dataset suitable for:
  - Data augmentation
  - Sensitivity analysis
  - Robustness testing of ML or optimization models

---

## Input Format

The input CSV must contain composition columns:

```text
E1, E2, E3, E4, E5
