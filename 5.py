import matplotlib.pyplot as plt
import numpy as np

# Data for the fifth question (Identify Winners)
labels = ['SVM WiFi', 'SVM Ethernet', 'k-NN WiFi', 'k-NN Ethernet']
cross_val_scores = [49.5, 50.0, 44.5, 48.0]
accuracy_scores = [66.6, 72.5, 60.0, 68.0]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(12, 6))  # Keep size same as previous images

# Bar chart for cross-validation scores
rects1 = ax.bar(x - width/2, cross_val_scores, width, label='Cross-Validation Score', color='#e3716e')
# Bar chart for accuracy scores
rects2 = ax.bar(x + width/2, accuracy_scores, width, label='Accuracy Score', color='#54beaa')

# Increase font size for labels, title, and ticks
ax.set_xlabel('Models and Connection Types', fontsize=14)
ax.set_ylabel('Scores (%)', fontsize=14)
ax.set_title('Model Performance for Identifying Winners', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=12)
ax.legend(loc='upper left', fontsize=12)
ax.tick_params(axis='y', labelsize=12)

# Attach a text label above each bar in rects1 and rects2, displaying its height
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # offset points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=12,
                    bbox=dict(boxstyle="round,pad=0.3", edgecolor='none', facecolor='white', alpha=0.6))

autolabel(rects1)  # Increase offset to move label higher
autolabel(rects2)

fig.tight_layout()

# Save the plot as an image file
plt.savefig('question5_winner_identification_larger_font.png')

plt.show()
