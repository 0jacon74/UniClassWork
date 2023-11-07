import csv

records = []
headings = []

def load_data(file_path):
    print("Loading Data...", end="")

    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        for values in csv_reader:
            records.append(values)


def run():
    load_data("titanic.csv")
    print(" Done!")
    print("Successfully loaded ", len(records), " records.")


run()