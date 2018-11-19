import csv
import json
import pandas as pd

txt = "KNMI_20161231.txt"

def CSV():
    with open(txt, 'r') as text:
        count = 0
        rows = []
        for line in text:
            count = count + 1
            if count >= 15:
                line = line.split(",")
                rows.append(line)
        for line in rows:
            line[4] = line[4].rstrip()
        for line in rows:
            for i in range(0, 5):
                line[i] = line[i].strip()
        out = csv.writer(open("KNMI.csv","w"),quoting=csv.QUOTE_ALL)
        for line in rows:
            out.writerow(line)
        dict = {}
        for line in rows:
            entry = {}
            entry["MED_T"] = line[2]
            entry["MIN_T"] = line[3]
            entry["MAX_T"] = line[4]
            dict[line[1]] = entry
        return(dict)

def JSON(dict):
    with open('KNMI.json', 'w') as outfile:
        json.dump(dict, outfile)

if __name__ == '__main__':
    dict = CSV()
    JSON(dict)
