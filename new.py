import numpy as np
import pandas as pd

data = pd.read_csv("president_heights.csv")
print(data.head())

height = np.array(data["height(cm)"])
print(height)

print("Average height is:",height.mean())
print("Maximum height is:",height.max())
print("Minimum height is:",height.min())
print("Standard deviation is:",height.std())


print("Median is:",np.median(height))
print("25th percentile is:",np.percentile(height,25))
print("75th percentile is:",np.percentile(height,75))



import matplotlib.pyplot as plt
import seaborn as sns


plt.hist(height)
plt.title("Height Distribution of Presidents")
plt.xlabel("height(cm)")
plt.ylabel("Number")
print(plt.show())