import sys
import csv
import getopt
from datetime import datetime
import time

same_date_list = []

argumentList = sys.argv

if len(argumentList) <= 3:
    print("Not enough arguments")
    exit(1)

try:
    arguments, values = getopt.getopt(argumentList[2:], "d:")
    
    for cur_arg, cur_val in arguments:
        if cur_arg in ['-d']:
            input_day = cur_val
            
    format  = '%Y-%m-%dT%H:%M:%S'

    time_dict = {}

    with open(sys.argv[1], 'r') as csv_file:
        read = csv.reader(csv_file)
        
        next(read)
        for row in read:
            print("time")
            print(row[1][:19])
            converted_datetime = datetime.strptime(row[1][:19], format)
            total_time = time.mktime(converted_datetime.timetuple())
            if row[1][:10] == input_day:
                if row[0] not in time_dict.keys():
                    time_dict[row[0]] = total_time
                same_date_list.append(row[0])

    print(same_date_list)

except getopt.error as err:
    print(str(err))
    exit(1)


cookie_dict = {}

# for cookie in same_date_list:
#     if cookie not in cookie_dict.keys():
#         cookie_dict[cookie] = 1
#     else:
#         cookie_dict[cookie] += 1

for cookie in same_date_list:
    if cookie not in cookie_dict.keys():
        cookie_dict[cookie] = 1
    else:
        cookie_dict[cookie] += 1

print(cookie_dict)
# list_dict = cookie_dict.items()
max_freq = max(cookie_dict.values())
max_list = [(key,time_dict[key]) for key, freq in cookie_dict.items() if freq == max_freq]
# b.sort(key=lambda x:x[1][2])
max_list = sorted(max_list, key=lambda x: x[1])[::-1]
for cookie in max_list:
    print(cookie[0])
