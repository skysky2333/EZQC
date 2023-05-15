import argparse
import numpy as np
from pbsq import parse_fastq_file, find_low_average_quality_positions

def process_fastq_file(file_path):
    # Process the .fastq file
    print(f"Processing file: {file_path}")

    quality_strings = []

    with open(file_path, 'r') as fastq_file:
        for _, _, quality_str in parse_fastq_file(fastq_file):
            quality_strings.append(quality_str)

    print(np.average([len(s) for s in quality_strings]))
    low_average_quality_positions = find_low_average_quality_positions(quality_strings)

    print(f"Low average quality positions: {low_average_quality_positions}")


def main():
    # Create the argparse object and define the arguments
    parser = argparse.ArgumentParser(description="EZQC FastQ Quality Analyzer")
    parser.add_argument('reads', metavar='READ', nargs='+', help='input .fastq file(s)')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Process each .fastq file
    for read in args.reads:
        process_fastq_file(read)

if __name__ == '__main__':
    main()
