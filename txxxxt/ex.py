import csv
import json


# Read the text file and convert it to a list of dictionaries
with open('newbackup.txt', mode='r',encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    print("***********************",csv_reader)
    data_list = [ row for row in csv_reader]
    print("*************",data_list)

# Write the list of dictionaries to a JSON file
# with open('data.json', mode='w') as file:
#     json.dump(data_list, file, indent=8)

import csv
import json

# read the CSV file
# with open('newbackup.txt', 'r',encoding="utf-8") as file:
#     reader = csv.DictReader(file)
#     print(reader)
#     rows = list(reader)
#     print("iiiiiioooopp",rows)

# convert CSV data to JSON
# with open('data.json', mode='w') as file:
#     a = json.dumps(rows)
#     print("**************************",a)
#     json.dump(a, file, indent=4)

# json_obj = json.dumps(rows)

# print JSON object
# print("jjjsonfile",json_obj)
