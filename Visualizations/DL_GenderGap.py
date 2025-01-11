import matplotlib.pyplot as plt
import numpy as np


# Data for gender and regional gap in digital literacy
regions = ["Urban", "Rural", "All"]
male_literacy = [47.7, 28.1, 34.2]  # 15-29 Years (Male)
female_literacy = [36.5, 14.5, 21.6]  # 15-29 Years (Female)

# Bar width and positions
x = np.arange(len(regions))
width = 0.4

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(x - width/2, male_literacy, width, label="Male", color="#1ABC9C")
plt.bar(x + width/2, female_literacy, width, label="Female", color="#FA8072")

# Add annotations
for i in range(len(regions)):
    plt.text(x[i] - width/2, male_literacy[i] + 1, f"{male_literacy[i]}%", ha="center", va="bottom", fontsize=10)
    plt.text(x[i] + width/2, female_literacy[i] + 1, f"{female_literacy[i]}%", ha="center", va="bottom", fontsize=10)

# Chart title and labels
plt.title("Gender Gap in Digital Literacy (Ages 15-29)", fontsize=14, fontweight="bold")
plt.ylabel("Percentage (%)", fontsize=12)
plt.xlabel("Region", fontsize=12)
plt.xticks(x, regions)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.6)

# Show the chart
plt.tight_layout()
plt.show()
