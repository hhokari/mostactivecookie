import sys
import csv

same_date_list = []

with open(sys.argv[1], 'r') as csv_file:
    read = csv.reader(csv_file)
    
    for row in read:
        if row[1][:10] == sys.argv[2]:
            same_date_list.append(row[0])

cookie_dict = {}

for cookie in same_date_list:
    if cookie not in cookie_dict.keys():
        cookie_dict[cookie] = 1
    else:
        cookie_dict[cookie] += 1

max_freq = max(cookie_dict.values())
max_list = [key for key, freq in cookie_dict.items() if freq == max_freq]

for cookie in max_list:
    print(cookie)
