# AirLabs-To-S3-Transfer

This project ingests data from [AirLabs API](https://airlabs.co/docs/flights) on Real-Time Flight Data request, used for finding out the information of the aircrafts in a certain location; in this case, used London Heathrow Airport as an example.

## Flight data example
```
[{
  "hex": "780695",
  "reg_number": "B-5545",
  "flag": "CN",
  "lat": 28.397377,
  "lng": 115.1008,
  "alt": 7078,
  "dir": 269,
  "speed": 775,
  "v_speed": -7.8,
  "squawk": "0205",
  "flight_number": "9429",
  "flight_icao": "CSH9429",
  "flight_iata": "FM9429",
  "dep_icao": "ZSPD",
  "dep_iata": "PVG",
  "arr_icao": "ZGHY",
  "arr_iata": "HNY",
  "airline_icao": "CSH",
  "airline_iata": "FM",
  "aircraft_icao": "B738",
  "updated": 1626153069,
  "status": "en-route"
}, {
  ...
}]

```

## Project Steps:

1. Pull the real-time flight data from AirLabs API.


## Other info

- Frequency:
- How to modify the data?

## Limitations

1. Using free api with limited filter features, causing extracting extra data that don't use.

