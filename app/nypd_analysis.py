import csv

# filename = "'./data/nypd-arrest-data-2018-1.csv'"
filename = "../data/small.csv"

def read_csv(filename):
    new_list = []
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            new_list.append(row)

    return new_list





nypd_list = read_csv(filename)

            