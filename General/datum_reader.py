import csv


def read_CSV(filepath):
    with open(filepath, "rb") as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def move_first_to_last(filepath):
    # moves the class form the first to the last index
    data = read_CSV(filepath)
    # I know this messes with file extentions, I'm sorry
    with open(filepath + "_fixed", "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            first = line.pop(0)  # take the first item off the list
            writer.writerow(line + [first])  # put it on the back


def move_last_to_first(filepath):
    # moves the class form the first to the last index
    data = read_CSV(filepath)
    # I know this messes with file extentions, I'm sorry
    with open(filepath + "_fixed", "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            last = line.pop()  # take the last item off the list
            writer.writerow([last] + line)  # put it on the front


# reads in data and formats them into a datum
# looks like this
# [[data, data, data...], [class]]
def read_in_data_csv_with_class_first(filepath):
    data = read_CSV(filepath)
    new_data = []
    for line in data:
        clas = line.pop(0)
        new_data.append([line, clas])
    return new_data
