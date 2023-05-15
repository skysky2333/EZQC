import argparse

def process_fastq_file(file_path):
    # Process the .fastq file
    print(f"Processing file: {file_path}")

def main():
    # Create the argparse object and define the arguments
    parser = argparse.ArgumentParser(description="EZQC takes in one or multiple .fastq file(s)")
    parser.add_argument('reads', metavar='READ', nargs='+', help='the .fastq file(s) to process')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Process each .fastq file
    for read in args.reads:
        process_fastq_file(read)

if __name__ == '__main__':
    main()
