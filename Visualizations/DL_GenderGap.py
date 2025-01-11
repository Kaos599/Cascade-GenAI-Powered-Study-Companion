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
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Set the background color for the figure and axis
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Create the bar chart
ax.bar(x - width/2, male_literacy, width, label="Male", color="#1ABC9C")
ax.bar(x + width/2, female_literacy, width, label="Female", color="#FA8072")

# Add annotations
for i in range(len(regions)):
    ax.text(x[i] - width/2, male_literacy[i] + 1, f"{male_literacy[i]}%", ha="center", va="bottom", fontsize=10, color="white")
    ax.text(x[i] + width/2, female_literacy[i] + 1, f"{female_literacy[i]}%", ha="center", va="bottom", fontsize=10, color="white")

# Chart title and labels
ax.set_title("Gender Gap in Digital Literacy (Ages 15-29)", fontsize=14, fontweight="bold", color="white")
ax.set_ylabel("Percentage (%)", fontsize=12, color="white")
ax.set_xlabel("Region", fontsize=12, color="white")
ax.set_xticks(x)
ax.set_xticklabels(regions, color="white")
ax.legend(facecolor='black', edgecolor='white', labelcolor='white')
ax.grid(axis="y", linestyle="--", alpha=0.6, color="#495057")

# Set tick parameters for both axes
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

# Set the axis lines to white
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')

# Remove the top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Show the chart
plt.tight_layout()
plt.show()
