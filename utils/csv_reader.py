import csv


def read_test_data_from_csv():
    test_data = []
    with open("../data/state_and_city.csv", newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=";")
        next(data)  # skip header row
        for row in data:
            print(row)
            state = row[0]
            city = row[1]
            state_and_city = (state, city)
            test_data.append(state_and_city)

    return test_data
