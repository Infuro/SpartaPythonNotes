import csv

def extract_csv(file_name):
    with open(file_name) as csvfile:
        return list(csv.reader(csvfile, delimiter=','))

def transform_user_details(csv_file_list):
    transformed_list = []
    for row in csv_file_list:
        transformed_list.append([row[i] for i in [1,2,4]])
    return transformed_list

def load_to_newfile(transformed_list, file):
    try:
        with open(file, 'a') as opened_file:
            [opened_file.write(f'{item[0]}, {item[1]}, {item[2]} \n') for item in transformed_list]
    except FileExistsError:
        print('file already exists')

load_to_newfile(
    transform_user_details(
        extract_csv('user_details.csv')),
            'updated_user_details.txt')