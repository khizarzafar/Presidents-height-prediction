import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
data = pd.read_csv("president_heights.csv")
data.dropna(subset=['height(cm)'], inplace=True) # Data Integrity check
print(data.head())

# 2. Extract values into a NumPy array
height = np.array(data["height(cm)"])
print(height)

# 3. Descriptive Statistics
stats = {
    "Mean": np.mean(height),
    "Median": np.median(height),
    "Std Dev": np.std(height),
    "25th Percentile": np.percentile(height, 25),
    "75th Percentile": np.percentile(height, 75),
}

print("--- Presidents Height Statistics ---")
for label, value in stats.items():
    print(f"{label:15}: {value:.2f} cm")


# 4. Advanced Visualization
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# Adding a KDE (smooth curve) over histogram
sns.histplot(height, bins=10, kde=True, color="skyblue")

plt.title("Distribution of Presidents' Heights", fontsize=15)
plt.xlabel("Height (cm)", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.axvline(
    np.median(height), color="red", linestyle="--", label=f"Median: {np.median(height)}"
)
plt.legend()
print(plt.show())

