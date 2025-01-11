import matplotlib.pyplot as plt
import numpy as np

# Data from the image
years = [2016, 2021]
market_size = [247, 1960] # Rounded to nearest 10 for cleaner visuals
users = [1.6, 9.6]

categories = ['Reskilling & Online Certifications', 'Primary & Secondary Supplemental Ed', 'Test Preparation']
market_size_2016 = [93, 73, 43] # USD Millions
cagr = [38, 60, 64]  # Compound Annual Growth Rate (%)

# --- Visualization 1: Market Size & Users Over Time ---
fig, ax1 = plt.subplots(figsize=(10, 6), facecolor='#007bff') # Figure background color to blue
ax1.set_facecolor('#007bff')

ax1.plot(years, market_size, marker='o', linestyle='-', linewidth=2, color='white')
ax1.set_xlabel('Year', color='white')
ax1.set_ylabel('Market Size (USD Millions)', color='white')
ax1.tick_params(axis='y', labelcolor='white')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.plot(years, users, marker='o', linestyle='--', linewidth=2, color='#17a2b8') #teal
ax2.set_ylabel('Users (Millions)', color='#17a2b8')  # we already handled the x-label with ax1
ax2.tick_params(axis='y', labelcolor='#17a2b8')


plt.title("India's Online Education Market Growth (2016-2021)", color='white', fontweight='bold', fontsize=14)
plt.xticks(years, color='white')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax1.spines['bottom'].set_color('white')
ax1.spines['left'].set_color('white')
ax1.tick_params(axis='x', colors='white')
ax2.spines['bottom'].set_color('white')
ax2.spines['left'].set_color('white')

plt.figtext(0.95, 0.02, "Source: KPMG and Google", ha='right', color='white') # Add source
plt.tight_layout()
plt.show()



# --- Visualization 2: Category Market Size (2016) and CAGR ---
plt.figure(figsize=(10, 6), facecolor='#007bff')
ax = plt.gca()
ax.set_facecolor('#007bff')

bar_width = 0.35
x_pos = np.arange(len(categories))

bars1 = ax.bar(x_pos, market_size_2016, bar_width, label='Market Size (2016, USD Millions)', color='white')
bars2 = ax.bar(x_pos + bar_width, cagr, bar_width, label='CAGR (%)', color='#17a2b8')

ax.set_ylabel('USD Millions / Percentage', color='white')
ax.set_title('Category Breakdown (2016) and Projected Growth', color='white', fontweight='bold', fontsize=14)
ax.set_xticks(x_pos + bar_width / 2)
ax.set_xticklabels(categories, rotation=45, ha='right', color='white')
ax.tick_params(axis='y', labelcolor='white')
ax.legend(facecolor='#007bff', labelcolor='white')

# Annotations (Data values on bars)
for bar, value in zip(bars1, market_size_2016):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(value), ha='center', va='bottom', color='black')
for bar, value in zip(bars2, cagr):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(value), ha='center', va='bottom', color='black')

plt.figtext(0.95, 0.02, "Source: KPMG and Google", ha='right', color='white')
plt.tight_layout()
plt.show()