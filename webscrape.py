import requests
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

spreadsheet = client.open("SCWD - Scraping")
sheet = spreadsheet.sheet1

sheet.update("A1", [["Name", "Address", "Phone Number", "Website"]])

API_KEY = 'AIzaSyCfIwSY4iS4-9g_NGerNlVcnZQu3MBks7A'

location = '28.0836,-80.6081'
radius = 10000
keyword = 'restaurant'

nearby_search_url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&keyword={keyword}&key={API_KEY}'

response = requests.get(nearby_search_url)
businesses = response.json().get('results', [])

def get_business_details(place_id):
    details_url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,vicinity,formatted_phone_number,website&key={API_KEY}'
    
    details_response = requests.get(details_url)
    return details_response.json().get('result', {})

row = 2 
for business in businesses:
    name = business.get('name')
    address = business.get('vicinity')
    place_id = business.get('place_id')

    details = get_business_details(place_id)
    phone_number = details.get('formatted_phone_number', 'N/A')
    website = details.get('website', 'N/A')

    sheet.update(f"A{row}", [[name, address, phone_number, website]])
    row += 1
    
    time.sleep(1)
