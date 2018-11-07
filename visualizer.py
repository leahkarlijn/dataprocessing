#!/usr/bin/env python
# Name:
# Student number:
"""
This script visualizes data obtained from a .csv file
"""

import csv
import matplotlib.pyplot as plt

# Global constants for the input file, first and last year
INPUT_CSV = "movies.csv"
START_YEAR = 2008
END_YEAR = 2018

average_dict = {str(key): [] for key in range(START_YEAR, END_YEAR)}
data_dict = {str(key): [] for key in range(START_YEAR, END_YEAR)}
with open(INPUT_CSV, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        year = row['Year']
        rating = float(row['Rating'])
        if int(year) in range(START_YEAR, END_YEAR):
            data_dict[year].append(rating)
            average = round(sum(data_dict[year])/ len(data_dict[year]), 1)
            average_dict[year] = average


# Global dictionary for the data

if __name__ == "__main__":
  plt.plot(average_dict.keys(), average_dict.values(), linestyle='-', marker='*', color='darkmagenta')
  plt.ylabel("year", color='b')
  plt.xlabel("rating", color='b')
  plt.show()
