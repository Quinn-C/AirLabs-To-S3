""" Functions to dump data into csv files"""

import csv

def to_csv(cleaned_data: list) -> None:
    """Transform data from python list to csv file directly"""
    with open("instance/flight_data.csv", "w", encoding="UTF-8") as csv_file:
        csv_columns = [
            "latitude", "longitude", "airline_country",
            "dep_airport", "arr_airport"
        ]
        writer = csv.DictWriter(csv_file, csv_columns, restval="Null")
        writer.writeheader()
        for row in cleaned_data:
            writer.writerow(row)
