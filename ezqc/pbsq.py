import numpy as np

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

def run_pbsq(quality_strings, average_length):

    average_quality_scores = calculate_average_quality_scores(quality_strings)
    average_quality_scores = average_quality_scores[:int(average_length)]

    avg_score = np.average(average_quality_scores)

    print(average_quality_scores)

    if (avg_score < 20):
        print(f"X | Per base sequence quality NOT pass. Average quality score {avg_score:.2f}")

    return