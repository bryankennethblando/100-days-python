import numpy as np

# sample data sets to be used for caluculating the std
random_data_set = [
    (5, 6, 7, 8, 9, 10, 11, 15), # customer's waiting time
    (3, 5, 7, 8, 12), # time of catching the falling ruler
    (6, 9, 12, 12, 15, 18) # battery life in hours
]

for i in range(len(random_data_set)):
    data_set = np.array(random_data_set[i])

    # calculationg the sum of each data_set
    sum_per_row = np.sum(data_set)

    # calculating the mean
    mean_per_row = np.round(np.mean(data_set))

    # variance
    variance_per_row = np.round(np.var(data_set, ddof=1), 2)

    # standard deviation st_dev
    std_dev_per_row = np.round(np.std(data_set, ddof=1), 2)

    # printing the result
    print(f'Data_set: {i}')
    print(f'The sample Data_set: {random_data_set[i]}')
    print(f'Sum: {sum_per_row}')
    print(f'Mean: {mean_per_row}')
    print(f'Variance: {variance_per_row}')
    print(f'Standard_dev: {std_dev_per_row}\n')
    