import matplotlib.pyplot as plt
import numpy as np

# Data for the fourth question (Identify Minigames)
labels = ['SVM WiFi', 'SVM Ethernet', 'k-NN WiFi', 'k-NN Ethernet']
cross_val_scores = [84.6, 92.1, 95.2, 93.0]
accuracy_scores = [86.4, 95.5, 100.0, 96.5]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(12, 6))

# Bar chart for cross-validation scores
rects1 = ax.bar(x - width/2, cross_val_scores, width, label='Cross-Validation Score', color='#e3716e')
# Bar chart for accuracy scores
rects2 = ax.bar(x + width/2, accuracy_scores, width, label='Accuracy Score', color='#54beaa')

# Add some text for labels, title, and custom x-axis tick labels, etc.
ax.set_xlabel('Models and Connection Types')
ax.set_ylabel('Scores (%)')
ax.set_title('Model Performance for Identifying Minigames')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Attach a text label above each bar in rects1 and rects2, displaying its height
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

# Save the plot as an image file
plt.savefig('question4_minigames_identification.png')

plt.show()
