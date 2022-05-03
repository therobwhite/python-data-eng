import csv


def read_csv(filename):
    new_list = []
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            new_list.append(row)

    return new_list


def sort_ofns_desc(nypd_list):
    ofns_dict = {}
    for row_dict in nypd_list:
        key = row_dict["OFNS_DESC"]
        if key in ofns_dict.keys():
            count =  ofns_dict[key]
            count += 1 
            ofns_dict.update({key: count})
        # If this exists as a key in OFNS_DESC Dictionary then add to value or create key
        else:
            ofns_dict[key] = 1

    sorted_tuple  = sorted(ofns_dict.items(), key=lambda x:x[1], reverse=True)

    return sorted_tuple


if __name__ == "__main__" :       
    # filename = "../data/nypd-arrest-data-2018-1.csv"
    filename = "../data/small.csv"

    nypd_list = read_csv(filename)
    ofns_sorted_tuple = sort_ofns_desc(nypd_list)

    print(ofns_sorted_tuple)

    print("First 10 entries are:-")
    print(ofns_sorted_tuple[0:10])
    




            