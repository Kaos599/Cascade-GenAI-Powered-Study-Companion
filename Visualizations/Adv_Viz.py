import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample Data (Replace with your actual data)
data = {
    'Category': ['Personalized Learning', 'Free Access', 'Adaptive Features', 'Comprehensive Resources', 'User Feedback Integration'],
    'Importance': [95, 90, 85, 80, 75],  # Example importance scores (out of 100)
    'Usage': [88, 92, 78, 85, 70], # Example usage percentages
    'User Age': [20, 22, 19, 21, 23], # Example user age for demo
    'Learning Style': ['Visual', 'Auditory', 'Kinesthetic', 'Visual', 'Auditory']
}
df = pd.DataFrame(data)

# --- Visualization 1: Bar Chart (Feature Importance) ---
plt.figure(figsize=(10, 6), facecolor='black')  # Set figure background color
ax = plt.gca()
ax.set_facecolor('black')

bars = plt.bar(df['Category'], df['Importance'], color='#1ABC9C')  # Teal color for positive values
plt.title('Key Features and Their Importance', color='white', fontsize=16, fontweight='bold')
plt.xlabel('Features', color='white')
plt.ylabel('Importance Score (out of 100)', color='white')

# Annotations (Data values on bars)
for bar, value in zip(bars, df['Importance']):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(value), ha='center', va='bottom', color='white')

# Customize axes and spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
ax.yaxis.grid(color='#495057', linestyle='--') # Add dashed gridlines

plt.tight_layout()  # Adjust layout to prevent labels from overlapping
plt.show()


# --- Visualization 2: Pie Chart (Usage Distribution) ---
plt.figure(figsize=(8, 8), facecolor='black')
ax = plt.gca()
ax.set_facecolor('black')

colors = ['#1ABC9C', '#17A2B8', '#FA8072', '#FF7F50', '#495057']  # Use your color palette
plt.pie(df['Usage'], labels=df['Category'], autopct='%1.1f%%', startangle=90, colors=colors, textprops={'color': 'white'})
plt.title('Usage Distribution of CASCADE Features', color='white', fontsize=16, fontweight='bold')

# Customize Legend
plt.legend(loc="lower right", facecolor='black', labelcolor='white') # Set background to black, text white


plt.show()



# --- Visualization 3: Histogram (User Age)---

plt.figure(figsize=(8, 6), facecolor='black')
ax = plt.gca()
ax.set_facecolor('black')


plt.hist(df['User Age'], bins=5, color='#1ABC9C', edgecolor='white') # Teal histogram
plt.title('Distribution of User Ages', color='white', fontsize=16, fontweight='bold')
plt.xlabel('User Age', color='white')
plt.ylabel('Number of Users', color='white')

# Customize axes and spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.tick_params(axis='both', colors='white')


plt.show()


# --- Visualization 4: Heatmap (Feature Importance by Category)---
# (Requires restructuring data if you have subcategories)

categories = df['Category'].unique()
features = df['Category'].unique() # Replace with your actual features

importance_matrix = np.random.rand(len(categories), len(features)) * 100 # Replace with your importance data

plt.figure(figsize=(10, 8), facecolor='black')
ax = plt.gca()
ax.set_facecolor('black')


plt.imshow(importance_matrix, cmap='viridis', interpolation='nearest')  # Use a suitable colormap
plt.colorbar(label='Importance Score')

plt.xticks(np.arange(len(features)), features, rotation=45, ha='right', color='white')
plt.yticks(np.arange(len(categories)), categories, color='white')

plt.title('Feature Importance by Category', color='white', fontsize=16, fontweight='bold')
plt.xlabel('Features', color='white')
plt.ylabel('Categories', color='white')

plt.tight_layout()
plt.show()