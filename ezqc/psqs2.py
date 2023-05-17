import numpy as np
import matplotlib.pyplot as plt

def phred33_to_q(qual_string):
    return [ord(ch) - 33 for ch in qual_string]

def mean_qual_score(qual_string):
    qual_scores = phred33_to_q(qual_string)
    return np.mean(qual_scores)

def run_psqs2(quality_strings):
# Calculate mean quality scores for each sequence
    mean_qual_scores = [mean_qual_score(qual_string) for qual_string in quality_strings]

    # Set up bins for the x-axis (mean sequence quality)
    bin_edges = np.arange(0, np.ceil(max(mean_qual_scores)) + 1, 1)

    # Calculate the frequency (counts) for each bin
    counts, _ = np.histogram(mean_qual_scores, bins=bin_edges)

    proportion_low_quality = sum(mqs < 20 for mqs in mean_qual_scores) / len(mean_qual_scores)
    print(proportion_low_quality)
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.bar(bin_edges[:-1], counts, width=1, edgecolor="k", alpha=0.7)
    plt.xlabel("Mean Sequence Quality(Phred scores)")
    plt.ylabel("Number of Sequences")
    plt.title("Per Sequence Quality Scores")
    plt.xticks(bin_edges)
    plt.grid(True, linestyle='--', alpha=0.5)

    # Save and/or display the plot
    plt.savefig("ezqc_output/per_sequence_quality_scores.png")
    # plt.show()


