def phred33_to_q(quality_str):
    return [ord(ch) - 33 for ch in quality_str]

def calculate_average_quality_scores(quality_strings):
    num_sequences = len(quality_strings)
    max_length = max(len(qstr) for qstr in quality_strings)
    position_sums = [0] * max_length

    for qstr in quality_strings:
        for i, q in enumerate(phred33_to_q(qstr)):
            position_sums[i] += q

    average_quality_scores = [total / num_sequences for total in position_sums]

    return average_quality_scores
