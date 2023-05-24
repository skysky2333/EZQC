import matplotlib.pyplot as plt
from collections import Counter
from .color_print import print_color
import numpy as np

def calculate_duplication_levels(sequences):
    # Use Counter to get the frequency of each sequence
    sequence_counts = Counter(sequences)

    # Bin the counts into duplication levels
    duplication_levels = Counter()
    for count in sequence_counts.values():
        if count == 1:
            duplication_levels['1'] += 1
        elif count == 2:
            duplication_levels['2'] += 1
        elif count <= 10:
            duplication_levels['3-10'] += 1
        elif count <= 50:
            duplication_levels['11-50'] += 1
        elif count <= 100:
            duplication_levels['51-100'] += 1
        elif count <= 500:
            duplication_levels['101-500'] += 1
        elif count <= 1000:
            duplication_levels['501-1000'] += 1
        elif count <= 5000:
            duplication_levels['1001-5000'] += 1
        elif count <= 10000:
            duplication_levels['5001-10000'] += 1
        else:
            duplication_levels['>10000'] += 1
    
    # Compute percentages
    total_sequences = len(sequences)
    for level in duplication_levels:
        duplication_levels[level] /= total_sequences / 100  # convert to percentage

    return duplication_levels

def plot_duplication_levels(duplication_levels):
    # Sort keys by duplication level
    sorted_keys = sorted(duplication_levels.keys(), key=lambda x: float(x.split('-')[0]) if '-' in x else (float('inf') if x[0] == '>' else float(x)))

    fig, ax1 = plt.subplots()

    # Plot a line chart of duplication levels
    ax1.plot(sorted_keys, [duplication_levels[key] for key in sorted_keys], color='b', label='Percentage of Sequences')
    ax1.set_xlabel("Duplication Level")
    ax1.set_ylabel("Percentage of DeDuplicated Sequences (%)", color='b')

    # Create second y-axis for percent of total sequences
    ax2 = ax1.twinx()
    ax2.plot(sorted_keys, [duplication_levels[key] for key in sorted_keys], color='r', label='Percent of Total Sequences')
    ax2.set_ylabel('Percent of Total Sequences (%)', color='r')

    fig.tight_layout()
    plt.title("Sequence Duplication Levels")
    # Save and/or display the plot
    # plt.show()
    plt.savefig("ezqc_output/Sequence_Duplication_Level.png")


def run_sdl7(sequences):
    # print("running function 7: Sequence Duplication Levels")
    duplication_levels = calculate_duplication_levels(sequences)
    plot_duplication_levels(duplication_levels)

# if (proportion_low_quality > 0.01):
#         print_color(f"X | Per sequence quality score NOT pass. Because proportion of low quality is \
#                     {100*proportion_low_quality:.2f} %, which is more than 1%","red")
#     else:
#         print_color(f"O | Per sequence quality pass. Proportion of low quality is {100*proportion_low_quality:.2f} %, \
#                     which is less than 1%","green")
