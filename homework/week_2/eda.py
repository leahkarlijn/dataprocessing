import csv

input_csv = "input.csv"

def get_data(filename):
    with open(input_csv, 'r') as csvFile:
        reader = csv.reader(csvFile)
        # skip empty rows
        for row in reader:
            if row:
                print(row)
                # check for left out data (google) 

if __name__ == '__main__':

    data = get_data(input_csv)
