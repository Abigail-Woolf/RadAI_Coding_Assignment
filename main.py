# Import Dependancies
from fastapi import FastAPI, Query, HTTPException
import json
from typing import List
from geopy.distance import geodesic

# gmaps = googlemaps.Client(key="AIzaSyDB0OOlW59HF84npZaKGd5VU6lQTcpV-N8")

# Load the json food truck data
with open("applicants.json", "r") as f:
    applicants = json.load(f)

# Instantiate app object
app = FastAPI()

#Build get request that searches for applicants by name, street or status of application
@app.get("/search/")
def search_applicants(applicant: str = None, street: str = None, status: str = None):
 
    results = []
    for applicant_data in applicants:
        if (applicant is None or applicant.lower() in applicant_data["applicant"].lower()) and \
           (street is None or street.lower() in applicant_data["address"].lower()) and \
           (status is None or status.lower() == applicant_data["status"].lower()):
            results.append(applicant_data)
    return results

# Build get request that finds the 5 nearest food trucks given lat. and long.
@app.get("/nearest_coordinates/")
def get_nearest_coordinates(latitude: float, longitude: float, include_all: bool = False) -> List[dict]:
    if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
        raise HTTPException(status_code=400, detail="Invalid latitude or longitude")
    
    if not include_all:
        filtered_locations = applicants
    else:
        filtered_locations = [loc for loc in applicants if loc.get("status") == "APPROVED"]

    sorted_coordinates = sorted(
        filtered_locations,
        key=lambda location: geodesic(
            (latitude, longitude), (location["latitude"], location["longitude"])
        ).kilometers,
    )[:5]

    return sorted_coordinates