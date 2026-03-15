import numpy as np

sample_data = [
    [24, 31, 12, 38, 12, 15],
    [5, 28, 16, 32, 5, 16, 48, 29, 5, 35],
    [53, 13, 34, 41, 26, 61, 34, 13, 69],
    [85, 58, 72, 85, 46, 93],
    [92, 63, 22, 80, 63, 71, 44, 35],
    [39, 82, 74, 96, 64, 52, 74],
    [72, 43, 15, 66, 32, 72, 52, 19, 28, 81],
    [40, 90, 36, 68, 90, 11, 88, 54],
    [12, 46, 32, 18,41, 46, 26],
    [63, 40, 51, 70, 36, 21, 51, 19, 28],
]

for i in range(len(sample_data)):
    calculation = np.array(sample_data[i])
    print(f"{i} mean: {np.round(np.mean(calculation), 2)}")
    print(f"{i} median: {np.median(calculation)}")
    print(f"{i} mode: {np.max(calculation) - np.min(calculation)}")
    print(" ")