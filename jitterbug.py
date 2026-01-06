import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("color_quinary_5%_E.csv")

composition_cols = ["E1", "E2", "E3", "E4", "E5"]

# Jitter strength (tune this)
sigma = 0.005  # 0.5 at.% noise

rng = np.random.default_rng(seed=42)

# Add Gaussian jitter
jitter = rng.normal(
    loc=0.0,
    scale=sigma,
    size=df[composition_cols].shape
)

jittered = df[composition_cols].values + jitter

# Enforce non-negativity
jittered = np.clip(jittered, 0.0, None)

# Renormalize so each row sums to 1
jittered /= jittered.sum(axis=1, keepdims=True)

# Replace compositions
df_jittered = df.copy()
df_jittered[composition_cols] = jittered

# Save
df_jittered.to_csv("color_quinary_5%_E2.csv", index=False)
