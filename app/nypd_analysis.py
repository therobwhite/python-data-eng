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

def count_arrests_by_age(nypd_list):
    age_group_dict = {}
    for row_dict in nypd_list:
        (age_key, pd_key)   = row_dict["AGE_GROUP"], row_dict["PD_CD"]
        if age_key in age_group_dict.keys():
            if pd_key in age_group_dict[age_key].keys():
                count = age_group_dict[age_key][pd_key]
                count += 1
                age_group_dict[age_key].update({pd_key: count})
            else:
                age_group_dict[age_key][pd_key] = 1
        else:
            # we have a new age group so start from 1
            age_group_dict[age_key] = {pd_key: 1}

    return age_group_dict


def write_csv_file(nypd_list, search_arg, output_filepath):
    filtered_list = [ row_dict for row_dict in nypd_list if row_dict["OFNS_DESC"].startswith(search_arg) ]
    print(filtered_list)
    with open(output_filepath, mode='w') as report_file:
        fieldnames = nypd_list[0].keys()
        writer = csv.DictWriter(report_file, fieldnames=fieldnames)
        writer.writeheader()
        for row_dict in filtered_list:
            writer.writerow(row_dict)



if __name__ == "__main__" :       
    # filename = "../data/nypd-arrest-data-2018-1.csv"
    # filename = "../data/small.csv"
    filename = "../data/medium.csv"

    nypd_list = read_csv(filename)
    ofns_sorted_tuple = sort_ofns_desc(nypd_list)

    print(ofns_sorted_tuple)

    print("First 10 entries are:-")
    print(ofns_sorted_tuple[0:10])

    age_group_dict = count_arrests_by_age(nypd_list)
    
    #TODO Find the 4th greatest number of arrests by PD_CD for each age group and output to the console
    print('\n\nfind 4th greatest by age group')


    for key in age_group_dict.keys():
        sorted_tuple = sorted(age_group_dict[key].items(), key=lambda x:x[1], reverse=True)
        print(f'{key} \t {sorted_tuple}')
        # print(sorted_tuple[3])

    write_csv_file(nypd_list, "BU", "./report.csv")






            