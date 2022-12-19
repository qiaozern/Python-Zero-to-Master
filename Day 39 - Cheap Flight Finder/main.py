from datetime import datetime, timedelta
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# set the departure code
ORIGIN_IATA_CODE = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

# check the spreadsheet that 'iataCode' column is empty. If yes, search the city code from the tequila API and update the spreadsheet with its city codes.
if sheet_data[0]['iataCode'] == "":
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])
    
    # print the sheet_data
    print(f"sheet_data: {sheet_data}")
    
    # update destination_data in DataManager Class
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
    
# create variable for contain datetime for tomorrow and 6 months later
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(30 * 6))

for destination in sheet_data:
    flight = flight_search.check_flight(
        ORIGIN_IATA_CODE, 
        destination['iataCode'], 
        from_time=tomorrow, 
        to_time=six_months_from_today
    )
    
    if flight.price < destination['lowestPrice']:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )