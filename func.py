import sys
import csv
import getopt
from datetime import datetime
import time
import logging

same_date_list = []

argumentList = sys.argv

# check for sufficient number of arguments
if len(argumentList) <= 3:
    raise TypeError("wrong number of arguments")

try:
    arguments, values = getopt.getopt(argumentList[2:], "d:")
    
    for cur_arg, cur_val in arguments:
        # if d parameter found, input_day is set to parameter argument (date)
        if cur_arg in ['-d']:
            input_day = cur_val
            
    format  = '%Y-%m-%dT%H:%M:%S'

    # key: cookie, val: total number of seconds
    time_dict = {}

    try:
        with open(sys.argv[1], 'r') as csv_file:
            read = csv.reader(csv_file)

            # skip header of csv file
            next(read)
            for row in read:
                # str -> datetime
                converted_datetime = datetime.strptime(row[1][:19], format)

                # convert to total number of seconds for easier comparison for later
                total_time = time.mktime(converted_datetime.timetuple())
                if row[1][:10] == input_day:
                    if row[0] not in time_dict.keys():
                        time_dict[row[0]] = total_time
                    same_date_list.append(row[0])

            # list being empty implies, invalid date provided       
            if len(same_date_list) == 0:
                raise ValueError("inputted date does not exist")

    # invalid file provided
    except IOError as e:
        logging.exception(e)
        exit(1)


except getopt.error as err:
    print(str(err))
    exit(1)


cookie_dict = {}

# determine frequencies of cookies
for cookie in same_date_list:
    if cookie not in cookie_dict.keys():
        cookie_dict[cookie] = 1
    else:
        cookie_dict[cookie] += 1


# get max frequency
max_freq = max(cookie_dict.values())

# max_list = [(cookie, total number of seconds)]
max_list = [(key,time_dict[key]) for key, freq in cookie_dict.items() if freq == max_freq]

# sort by total number of seconds, reversed for descending order
max_list = sorted(max_list, key=lambda x: x[1])[::-1]
for cookie in max_list:
    print(cookie[0])
