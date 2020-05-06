import csv
from Country import *


class Manager:
    dates = []
    countries = dict()

    def __init__(self, file: str):
        self.file = file
        self.parse()

    def parse(self):  # Process csv file into country objects
        csv_reader = csv.reader(open(self.file), delimiter=',')
        index = 0
        for row in csv_reader:
            if index != 0 and not (str(row[1]) in self.countries):
                self.countries[str(row[1])] = Country(row[1], row[4:])
            elif str(row[1]) in self.countries:  # Need to take care of duplicates in the case of territories
                self.countries[str(row[1])].merge(row[4:])
            else:
                self.dates = row[4:]
                index = index + 1


# Access country by calling name from dictionary
manager = Manager("time_series_covid19_confirmed_global.csv")  # Use with countries with high rates of testing
index = 0
for item in manager.countries['France'].get_weekly_case_acceleration():  # Spain closed on 3/14/20
    print(manager.dates[index], end=" ")                                 # Portugal closed on 3/14/20
    print(item)                                                          # Italy closed on 3/09/20
    index = index + 7                                                    # France closed on 3/17/20

