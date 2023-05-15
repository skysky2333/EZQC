# fastq_utils.py

def phred33_to_q(quality_str):
    return [ord(ch) - 33 for ch in quality_str]

def find_low_average_quality_positions(quality_strings, threshold=20):
    num_sequences = len(quality_strings)
    max_length = max(len(qstr) for qstr in quality_strings)
    position_sums = [0] * max_length

    for qstr in quality_strings:
        for i, q in enumerate(phred33_to_q(qstr)):
            position_sums[i] += q

    low_average_quality_positions = [
        i + 1 for i, total in enumerate(position_sums)
        if total / num_sequences < threshold
    ]

    return low_average_quality_positions

def parse_fastq_file(file_obj):
    while True:
        header = file_obj.readline().strip()
        if not header:
            break
        sequence = file_obj.readline().strip()
        file_obj.readline()
        quality_str = file_obj.readline().strip()
        yield header, sequence, quality_str
