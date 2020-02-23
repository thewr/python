# Copyright 2017, 2013, 2011 Pearson Education, Inc., W.F. Punch & R.J.Enbody
# highest mileage data
import csv

def create_mileage_list(epa_file):
    """Create a list of cars and mileage from epa_file."""
    mileage_list = []
    reader = csv.reader(epa_file)
    count = 0
    for line_list in reader:
        if count == 0:
            print(line_list)
        count += 1
        mileage_list.append(line_list[2])  # get make of auto
    return mileage_list

#################################

# 1. open EPA data file
epa_file = open("epaData_2.csv", "r")
mileage_list = create_mileage_list(epa_file)

print(mileage_list)
