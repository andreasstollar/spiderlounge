#!/usr/bin/env python3

import csv
import io

with open('Spiderlounge_Set_Eagles_2023-07-08.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('"{}","{}","{}","{}","{}"'.format(row[0], row[5], row[6], row[7], row[8]))
            line_count += 2
        elif "Yes" == (row[4]):
            print('"{}","{}","{}","{}","{}"'.format(row[0], row[5], row[6], row[7], row[8]))
            line_count += 1
