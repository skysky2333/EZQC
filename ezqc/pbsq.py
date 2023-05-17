import numpy as np

threhold = 20

def phred33_to_q(quality_str):
    return [ord(ch) - 33 for ch in quality_str]

def find_largest_range(lst):
    start = end = 0
    largest_start = largest_end = 0
    largest_range_length = 0

    for i, num in enumerate(lst):
        print(num, end=" ")
        print(start, end=" ")
        print(end, end=" ")
        if num > threhold:
            if start == end:
                start = end = i
                end = i+1
            else:
                end = i
        else:
            if end - start > largest_range_length:
                largest_start = start
                largest_end = end
                largest_range_length = end - start
            start = end = i + 1

    # Check if the last range is the largest
    if end - start > largest_range_length:
        largest_start = start
        largest_end = end
        largest_range_length = end - start

    return largest_start, largest_end

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


    if (avg_score < threhold*0.75):
        print(f"X | Per base sequence quality NOT pass. Low average quality score of {avg_score:.2f}")
    elif (all(x >= threhold for x in average_quality_scores)):
        print(f"O | Per base sequence quality pass. With high average quality score of {avg_score:.2f}")
    else:
        start, end = find_largest_range(average_quality_scores)
        print(f"- | Per base sequence quality can be improved. With high quality reads from position {start} to {end}")

        
    return