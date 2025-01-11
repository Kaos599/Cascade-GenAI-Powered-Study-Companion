import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample Data (Your Heatmap Data)
categories = ['Personalized Learning', 'Free Access', 'Adaptive Features', 'Comprehensive Resources', 'User Feedback Integration']
features = ['Personalized Learning', 'Free Access', 'Adaptive Features', 'Comprehensive Resources', 'User Feedback Integration']
importance_matrix = np.random.rand(len(categories), len(features)) * 100  # Example data

# Create the Heatmap
plt.figure(figsize=(10, 8), facecolor='black')
ax = plt.gca()
ax.set_facecolor('black')

plt.imshow(importance_matrix, cmap='viridis', interpolation='nearest')
plt.colorbar(label='Importance Score')

# Straight and Potentially Multi-line x-axis labels
plt.xticks(np.arange(len(features)), [f.replace(' ', '\n') for f in features], rotation=90, ha='center', color='white')  # Rotate 90 degrees and center
plt.yticks(np.arange(len(categories)), categories, color='white') # Keep y-axis labels as they are


plt.title('Feature Importance by Category', color='white', fontsize=16, fontweight='bold')
plt.xlabel('Features', color='white')
plt.ylabel('Categories', color='white')

plt.tight_layout()
plt.show()