import matplotlib.pyplot as plt
import numpy as np

# Data for state-wise digital divide in internet skills
states = ["Goa", "Kerala", "Tamil Nadu", "Telangana", 
          "Uttar Pradesh", "Chhattisgarh", "Tripura", "Meghalaya"]
percentages = [65.7, 53.4, 48.0, 47.2, 16.0, 11.9, 8.2, 7.5]
national_average = 28.5

# Colors for bars based on whether they are above or below the national average
colors = ["#17A2B8" if val >= national_average else "#FF7F50" for val in percentages]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Set the background color for the figure and axis
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Create the bar chart
bars = ax.bar(states, percentages, color=colors, edgecolor="black")

# Add a horizontal line for the national average
ax.axhline(y=national_average, color="white", linestyle="--", linewidth=1.5, label="National Average")

# Annotate bars with percentages
for bar, value in zip(bars, percentages):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f"{value:.1f}%", 
             ha="center", va="bottom", fontsize=10, color="white")

# Chart title and labels
ax.set_title("State-wise Digital Divide in Internet Skills (Ages 15-29)", fontsize=14, fontweight="bold", color="white")
ax.set_ylabel("Percentage (%)", fontsize=12, color="white")
ax.set_xlabel("States", fontsize=12, color="white")
ax.legend(facecolor='black', edgecolor='white', labelcolor='white')
ax.grid(axis="y", linestyle="--", alpha=0.6, color='white')

# Set tick parameters for both axes
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

# Set the axis lines to white
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')

# Show the chart
plt.tight_layout()
plt.show()
