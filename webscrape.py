import requests
import time

API_KEY = AIzaSyCfIwSY4iS4-9g_NGerNlVcnZQu3MBks7A

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

for business in businesses:
    name = business.get('name')
    address = business.get('vicinity')
    place_id = business.get('place_id')

    details = get_business_details(place_id)
    phone_number = details.get('formatted_phone_number', 'N/A')
    website = details.get('website', 'N/A')

    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"Phone Number: {phone_number}")
    print(f"Website: {website}")
    print("=" * 40)
    
    time.sleep(1)
