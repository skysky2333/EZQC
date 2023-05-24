# import matplotlib.pyplot as plt
# from color_print import print_color

# def compute_gc_content(sequences):
#     # Initialize a list to store GC content for each sequence
#     gc_content = []

#     # Iterate through each sequence
#     for seq in sequences:
#         # Compute the GC content for the current sequence
#         count_gc = sum(base in "GC" for base in seq)
#         gc_percent = 100 * count_gc / len(seq)

#         # Append the GC content to the list
#         gc_content.append(gc_percent)

#     # Return the list of GC content
#     return gc_content

# def plot_gc_content(gc_content):
#     # Sort the GC content
#     sorted_gc_content = sorted(gc_content)

#     # Create a line plot of the sorted GC content
#     plt.figure()
#     plt.plot(sorted_gc_content, range(len(sorted_gc_content)))
#     plt.title("Per sequence GC content")
#     plt.ylabel("Read number")
#     plt.xlabel("GC content (%)")

#     # Set the x-axis range from 0 to 100
#     plt.xlim([0, 100])

#     # Save and/or display the plot
#     plt.savefig("ezqc_output/per_sequence_GC_content.png")
#     # plt.show()
# def run_psgc4(sequences):
#     print("running function 4")
#     gc_content = compute_gc_content(sequences)
#     plot_gc_content(gc_content)

from Bio.SeqUtils import GC
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from .color_print import print_color
# need to pip install scipy

def compute_gc_content(sequences):
    gc_contents = [GC(seq) for seq in sequences]
    return gc_contents

def generate_plot(gc_contents):
    n_bins = 100
    plt.hist(gc_contents, bins=n_bins, density=True, alpha=0.6, color='g')

    mu, std = norm.fit(gc_contents)

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.figure()
    plt.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    plt.title(title)
    plt.xlim([0, 100])

    plt.xlabel('GC Content (%)')
    plt.ylabel('Frequency')
    # Save and/or display the plot
    plt.savefig("ezqc_output/per_sequence_GC_content.png")
    # plt.show()
# def compute_gc_content(sequences):
#     # Initialize a list to store GC content for each sequence
#     gc_content = []

#     # Iterate through each sequence
#     for seq in sequences:
#         # Compute the GC content for the current sequence
#         count_gc = sum(base in "GC" for base in seq)
#         gc_percent = 100 * count_gc / len(seq)

#         # Append the GC content to the list
#         gc_content.append(gc_percent)

#     # Return the list of GC content
#     return gc_content

# def generate_plot(gc_content):
#     # Sort the GC content
#     sorted_gc_content = sorted(gc_content)

#     # Create a line plot of the sorted GC content
#     plt.figure()
#     plt.plot(sorted_gc_content, range(len(sorted_gc_content)))
#     plt.title("Per sequence GC content")
#     plt.ylabel("Read number")
#     plt.xlabel("GC content (%)")

#     # Set the x-axis range from 0 to 100
#     plt.xlim([0, 100])

#     # Save and/or display the plot
#     plt.savefig("ezqc_output/per_sequence_GC_content.png")
#     # plt.show()

def detect_warnings_failures(gc_contents,sequences):
    mu, std = norm.fit(gc_contents)
    deviations = [abs(content - mu) for content in gc_contents]

    sum_deviation = sum(deviations)

    warning_threshold = 0.15 * len(sequences)
    failure_threshold = 0.30 * len(sequences)

    if sum_deviation > warning_threshold and sum_deviation <= failure_threshold:
        print_color("- | The sum of the deviations from the normal distribution represents more than 15% of the reads.","yellow")
    elif sum_deviation > failure_threshold:
        print_color("X | The sum of the deviations from the normal distribution represents more than 30% of the reads.","red")
    else:
        print_color("O | The sum of the deviations from the normal distribution are good","green")

def run_psgc4(sequences):
    # print("running function 4: Per sequence GC content")
    gc_contents = compute_gc_content(sequences)
    generate_plot(gc_contents)
    detect_warnings_failures(gc_contents,sequences)