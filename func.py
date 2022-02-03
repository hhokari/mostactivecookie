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

cur_max = 0
max_list = []

for key in cookie_dict.keys():
    cookie = cookie_dict[key]
    if cookie > cur_max:
        cur_max = cookie
        max_list = []
        max_list.append(key)
    elif cookie == cur_max:
        max_list.append(key)

for cookie in max_list:
    print(cookie)
