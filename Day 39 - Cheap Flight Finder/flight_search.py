import os
import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = os.environ("TEQUILA_API_KEY")

class FlightSearch:    
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        # # testing code by update spreadsheet column 'iataCode' as TESTING
        # code = "TESTING"
        # return code
        
        # create location endpoint, query, and header
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "term": city_name,
            "location_type": "city"
        }
        
        # get the response from API and return the city code
        response = requests.get(
            url=location_endpoint, 
            headers=headers,
            params=query
        )
        result = response.json()['locations']
        code = result[0]['code']
        return code
    
    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        # search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query
        )
        
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        
        flight_data = FlightData(
            price = data['price'],
            origin_airport=data['route'][0]['flyFrom'],
            origin_city=data['route'][0]['cityFrom'],
            destination_airport=data['route'][0]['flyTo'],
            destination_city=data['route'][0]['cityTo'],
            out_date=data['local_departure'].split("T")[0],
            return_date=data['local_arrival'].split("T")[0]
        )
        
        print(f"{flight_data.destination_city}: ??{flight_data.price}")
        
        return flight_data