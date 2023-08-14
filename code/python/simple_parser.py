#!/usr/bin/env python3

import csv
import io
import sys

file = sys.argv[1]

with open(file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('"{}","{}","{}","{}","{}"'.format(row[1], row[11], row[12], row[16], row[17]))
            line_count += 2
        elif "MUTUAL FUND OPEN END" == (row[0]): # These are always work $1.00
             print('"{}","{}","{}","1.00","=(C{}*D{})"'.format(row[1], row[11], row[12], line_count, line_count ))   
        elif len(row[1]) >=1 and "CASH" not in (row[1]):
            if "BRK/B" == (row[11]): # lookups fail, need to change '/' to '-' probably can make generic
                #print("ABBERATION")
                row[11] = "BRK-B"
            print('"{}","{}","{}","=STOCK(B{},0)","=(C{}*D{})"'.format(row[1], row[11], row[12], line_count, line_count, line_count ))
            line_count += 1
        elif "Total for Accounts" in (row[0]):
            line_count -= 1
            print('"Totals","","","","=SUM(E2:E{})"'.format(line_count))
            exit(0)
