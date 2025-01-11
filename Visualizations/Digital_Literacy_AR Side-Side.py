import matplotlib.pyplot as plt
import numpy as np

# Data for digital literacy by age group and region
age_groups = ["15-24 Years", "15-29 Years", "15+ Years"]
categories = ["Urban", "Rural", "All"]
male = {
    "15-24 Years": [44.2, 26.4, 31.8],
    "15-29 Years": [47.7, 28.1, 34.2],
    "15+ Years": [41.8, 23.4, 30.1],
}
female = {
    "15-24 Years": [35.3, 14.3, 20.7],
    "15-29 Years": [36.5, 14.5, 21.6],
    "15+ Years": [28.0, 11.7, 18.0],
}
person = {
    "15-24 Years": [40.2, 21.0, 26.8],
    "15-29 Years": [42.6, 22.0, 28.5],
    "15+ Years": [35.7, 18.5, 25.0],
}

# Bar width and positions
x = np.arange(len(categories))
width = 0.25

# Plot the grouped bar chart for each age group
fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)
fig.patch.set_facecolor('black')

for i, age_group in enumerate(age_groups):
    ax = axes[i]
    ax.set_facecolor('black')
    
    ax.bar(x - width, male[age_group], width, label="Male", color="#1ABC9C")
    ax.bar(x, female[age_group], width, label="Female", color="#FA8072")
    ax.bar(x + width, person[age_group], width, label="Person", color="#17A2B8")
    
    # Chart customization
    ax.set_title(f"Digital Literacy ({age_group})", fontsize=14, fontweight="bold", color="white")
    ax.set_xticks(x)
    ax.set_xticklabels(categories, color="white")
    ax.set_xlabel("Region", fontsize=12, color="white")
    if i == 0:
        ax.set_ylabel("Percentage (%)", fontsize=12, color="white")
    ax.grid(axis="y", linestyle="--", alpha=0.6, color="#495057")
    ax.legend(facecolor='black', edgecolor='white', labelcolor='white')
    
    # Set tick parameters for both axes
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    
    # Set the axis lines to white
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    
    # Remove the top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# Adjust layout and display
plt.tight_layout()
plt.show()
