# python-lokation-lookup

A beginner-friendly Python script that uses the [OpenGeo API](https://py4e-data.dr-chuck.net/opengeo?) to fetch detailed geolocation information based on a user-provided address.

This script was written as a part of my learning journey while studying Python, and it demonstrates how to work with HTTP requests, JSON data, and external APIs.

---

## What It Does

- Takes user input for a location (e.g. "USC", "South Federal University")
- Sends a request to the OpenGeo API
- Parses the returned JSON
- Prints out useful location data, such as:
  - Country and county
  - Display name
  - Latitude and longitude
  - Result type (e.g. "university", "city")
  - Time zone
  - Plus code

---

## Requirements

- Python 3.x  
(No external packages needed — just uses built-in libraries like `urllib`, `json`, and `ssl`)

---

## How to Run
- You’ll be prompted to enter an address. Type any place name, or type quit to exit.
