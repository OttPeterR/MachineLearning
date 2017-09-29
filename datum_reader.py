import numpy as np
import csv


# just reads it in as python arrays, must be converted later
def read_CSV(filepath, delimiter=','):
    with open(filepath, "r") as f:
        reader = csv.reader(f, delimiter=delimiter, quoting=csv.QUOTE_NONE)
        data_strings = list(reader)
        data = []
        for datum in data_strings:
            points = []
            for d in datum:
                points.append(float(d))
            data.append(points)
    return data


def move_first_to_last(filepath, delimiter=","):
    # moves the class form the first to the last index
    data = read_CSV(filepath)
    # I know this messes with file extentions, I'm sorry
    with open(filepath + "_fixed", "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=delimiter)
        for line in data:
            first = line.pop(0)  # take the first item off the list
            writer.writerow(line + [first])  # put it on the back


def move_last_to_first(filepath, delimiter=","):
    # moves the class form the first to the last index
    data = read_CSV(filepath, delimiter)
    # I know this messes with file extentions, I'm sorry
    with open(filepath + "_fixed", "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=delimiter)
        for line in data:
            last = line.pop()  # take the last item off the list
            writer.writerow([last] + line)  # put it on the front


# reads in data and formats them into a datum
# looks like this
# [[data, data, data...], [class]]
def read_in_data_csv_with_class_first(filepath, delimiter=","):
    data = read_CSV(filepath, delimiter)
    new_data = []
    for line in data:
        clas = line.pop(0)
        new_data.append([np.matrix(line), np.matrix(clas)])
    return new_data


def read_in_data_csv_with_class_last(filepath, delimiter=","):
    data = read_CSV(filepath, delimiter)
    new_data = []
    for line in data:
        clas = line.pop()
        new_data.append([np.matrix(line), np.matrix(clas)])
    return new_data


# expects a numpy array
def normalize_data(mat):
    num_cols = mat.shape[1]
    maxx = np.squeeze(np.asarray(mat[0].copy()))
    minn = np.squeeze(np.asarray(mat[0].copy()))

    # calculate min and max for each col
    for row_num in range(len(mat)):
        for col_num in range(num_cols):
            if(maxx[col_num] < mat[row_num, col_num]):
                maxx[col_num] = mat[row_num, col_num]
            if(minn[col_num] > mat[row_num, col_num]):
                minn[col_num] = mat[row_num, col_num]

    # compute ranges for each col
    rang = [0] * num_cols

    for index in range(num_cols):
        rang[index] = float(maxx[index] - minn[index])

    # normalize all the values, respective to other elements in the same col
    norm_mat = np.zeros(mat.shape)
    for row_num in range(len(mat)):
        for col_num in range(num_cols):
            # normalize: (val-min)/range
            norm_mat[row_num, col_num] = (
                (mat[row_num, col_num] - minn[col_num]) /
                rang[col_num])

    return norm_mat


def normalize_file(filepath, delimiter=','):
    data = read_CSV(filepath, delimiter=delimiter)
    norm_data = normalize_data(data)
    with open(filepath + "_normalized", "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=delimiter)
        for line in norm_data:
            writer.writerow(line)
