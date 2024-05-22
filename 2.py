import matplotlib.pyplot as plt
import numpy as np

# Data for the second question (Identify Game Collections)
labels = ['SVM WiFi', 'SVM Ethernet', 'k-NN WiFi', 'k-NN Ethernet']
cross_val_scores_switch = [99.1, 94.4, 98.2, 97.2]
cross_val_scores_vr = [93.3, 95.0, 75.0, 95.5]
accuracy_scores_switch = [96.3, 96.3, 96.3, 96.3]
accuracy_scores_vr = [75.0, 86.4, 75.0, 95.5]

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots(figsize=(12, 6))

# Bar chart for cross-validation scores (Switch)
rects1 = ax.bar(x - width, cross_val_scores_switch, width, label='Cross-Val Score Switch', color='#e3716e')
# Bar chart for accuracy scores (Switch)
rects2 = ax.bar(x, accuracy_scores_switch, width, label='Accuracy Switch', color='#54beaa')
# Bar chart for cross-validation scores (VR)
rects3 = ax.bar(x + width, cross_val_scores_vr, width, label='Cross-Val Score VR', color='#e3716e', alpha=0.6)
# Bar chart for accuracy scores (VR)
rects4 = ax.bar(x + 2*width, accuracy_scores_vr, width, label='Accuracy VR', color='#54beaa', alpha=0.6)

# Add some text for labels, title, and custom x-axis tick labels, etc.
ax.set_xlabel('Models and Connection Types')
ax.set_ylabel('Scores (%)')
ax.set_title('Model Performance for Identifying Game Collections')
ax.set_xticks(x + width / 2)
ax.set_xticklabels(labels)
ax.legend()

# Attach a text label above each bar in rects1, rects2, rects3, and rects4, displaying its height
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
autolabel(rects3)
autolabel(rects4)

fig.tight_layout()

# Save the plot as an image file
plt.savefig('game_collections_performance_fixed.png')

plt.show()
