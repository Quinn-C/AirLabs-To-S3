#!/usr/bin/env python3
''' Download the data with initial cleanup and export to a csv file'''

import csv
import requests
import params

API_PARAMS = params.API_PARAMS

HEATHROW_LFT_TOP = {
    'lat': 51.479717,
    'lng': -0.494472
}

HEATHROW_RGT_BTM = {
    'lat': 51.464106,
    'lng': -0.431946
}

def get_flight_data(api_params = API_PARAMS):
    ''' Download the real-time data from the data source api'''
    api_result = requests.get('https://airlabs.co/api/v9/flights', api_params)
    return api_result.json()['response']

# Define the conditions of the data filtration
def is_in_heathrow(flight_lat: float, flight_lng: float) -> bool:
    '''Check if the input flight is inside the Heathrow airport in real time'''
    if HEATHROW_RGT_BTM['lat'] < flight_lat < HEATHROW_LFT_TOP['lat']:
        if HEATHROW_LFT_TOP['lng'] < flight_lng < HEATHROW_RGT_BTM['lng']:
            return True
    return False

# Initiated a dictionary
FLIGHTS_DATA = {}

response_data = get_flight_data()


i = 0
# Filter the data and store them into the python dictionary
for flight in response_data:
    if is_in_heathrow(flight['lat'], flight['lng']):
        FLIGHTS_DATA[i] = flight
        i += 1
    else:
        continue


# New plan: Transform python dictionary to csv file directly
with open("flight_data.csv", "w", encoding = "UTF-8") as csv_file:
    csv_columns = ['hex',
                   'reg_number',
                   'flag',
                   'lat',
                   'lng',
                   'alt',
                   'dir',
                   'speed',
                   'v_speed',
                   'squawk',
                   'flight_number',
                   'flight_icao',
                   'flight_iata',
                   'dep_icao',
                   'dep_iata',
                   'arr_icao',
                   'arr_iata',
                   'airline_icao',
                   'airline_iata',
                   'aircraft_icao',
                   'updated',
                   'status']
    writer = csv.DictWriter(csv_file, csv_columns, restval = "Null")
    writer.writeheader()
    for flight in FLIGHTS_DATA.values():
        writer.writerow(flight)
