import matplotlib.pyplot as plt
import numpy as np

def plot_question(short_title, labels, cross_val_scores, accuracy_scores, file_name):
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
    ax.set_title(f'Model Performance for {short_title}', fontsize=16)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=12)
    ax.set_yticks(np.arange(30, 101, 10))
    ax.set_ylim(30, 105)
    ax.legend(loc='lower left', fontsize=12)
    ax.tick_params(axis='y', labelsize=12)

    # Attach a text label above each bar in rects1 and rects2, displaying its height
    def autolabel(rects, offset):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            if height >= 98:
                offset = 8  # Increase offset for values close to 100 to avoid overlap
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, offset),  # offset points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom',
                        fontsize=12,
                        bbox=dict(boxstyle="round,pad=0.3", edgecolor='none', facecolor='white', alpha=0.6))

    autolabel(rects1, 3)  # Increase offset to move label higher
    autolabel(rects2, 3)

    fig.tight_layout()

    # Save the plot as an image file
    plt.savefig(file_name)
    plt.show()

# Question 1 data
labels_q1 = ['SVM WiFi', 'SVM Ethernet', 'k-NN WiFi', 'k-NN Ethernet']
cross_val_scores_q1 = [96.4, 100.0, 99.6, 99.6]
accuracy_scores_q1 = [100.0, 98.3, 98.3, 98.3]
plot_question('Game Devices', labels_q1, cross_val_scores_q1, accuracy_scores_q1, 'question1_game_devices.png')

# Question 2 data
labels_q2 = ['SVM WiFi', 'SVM Ethernet', 'k-NN WiFi', 'k-NN Ethernet']
cross_val_scores_q2 = [99.1, 94.4, 98.2, 97.2]
accuracy_scores_q2 = [96.3, 96.3, 96.3, 96.3]
plot_question('Game Collections', labels_q2, cross_val_scores_q2, accuracy_scores_q2, 'question2_game_collections.png')

# Question 3 data
labels_q3 = ['SVM WiFi', 'SVM Ethernet', 'k-NN WiFi', 'k-NN Ethernet']
cross_val_scores_q3 = [93.3, 95.0, 75.0, 95.5]
accuracy_scores_q3 = [75.0, 86.4, 75.0, 95.5]
plot_question('Game Identification', labels_q3, cross_val_scores_q3, accuracy_scores_q3, 'question3_game_identification.png')

# Question 4 data
labels_q4 = ['SVM WiFi', 'SVM Ethernet', 'k-NN WiFi', 'k-NN Ethernet']
cross_val_scores_q4 = [84.6, 92.1, 95.2, 93.0]
accuracy_scores_q4 = [86.4, 95.5, 100.0, 96.5]
plot_question('Minigames Identification', labels_q4, cross_val_scores_q4, accuracy_scores_q4, 'question4_minigames_identification.png')

# Question 5 data
labels_q5 = ['SVM WiFi', 'SVM Ethernet', 'k-NN WiFi', 'k-NN Ethernet']
cross_val_scores_q5 = [49.5, 50.0, 44.5, 48.0]
accuracy_scores_q5 = [66.6, 72.5, 60.0, 68.0]
plot_question('Winner Identification', labels_q5, cross_val_scores_q5, accuracy_scores_q5, 'question5_winner_identification.png')