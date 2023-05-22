import matplotlib.pyplot as plt

def per_base_sequence_content(seqs):
    # Initialize a dictionary to hold our counts
    base_content = {'A': [], 'T': [], 'C': [], 'G': []}

    # Determine the length of the longest sequence
    max_length = max(len(seq) for seq in seqs)

    # Loop over each position up to the maximum length
    for i in range(max_length):
        # Initialize a dictionary to hold the counts for this position
        pos_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0, 'N': 0}
        
        # Loop over each sequence and count the bases at this position
        for seq in seqs:
            if i < len(seq):
                pos_counts[seq[i]] += 1
        
        # Calculate the percentage of each base at this position and add it to our base_content dictionary
        total_count = sum(pos_counts.values())
        for base in base_content.keys():
            base_content[base].append(pos_counts[base] / total_count * 100)

    return base_content



def plot_base_content(base_content):
    # Create the x-values for our plot (the position in the read)
    x_values = list(range(1, len(base_content['A'])+1))

    # Create a new figure
    plt.figure()

    # Plot the base content for each base 
    for base, y_values in base_content.items():
        plt.plot(x_values, y_values, label=base)

    # Add labels and a legend
    plt.xlabel('Position in read (bp)')
    plt.ylabel('Base content (%)')
    plt.legend()

    # Show the plot
    plt.savefig("ezqc_output/per_base_sequence_content_plot.png")
    #plt.show()

def run_pbsc3(seqs):
    plot_base_content(per_base_sequence_content(seqs))
