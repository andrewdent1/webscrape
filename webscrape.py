import requests

API_KEY = AIzaSyCfIwSY4iS4-9g_NGerNlVcnZQu3MBks7A

location = '28.0836,-80.6081'
radius = 10000
keyword = 'restaurant'

url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&keyword={keyword}&key={API_KEY}'

response = requests.get(url)

businesses = response.json().get('results', [])

for business in businesses:
    name = business.get('name')
    address = business.get('vicinity')
    rating = business.get('rating', 'No rating')
    print(f"Name: {name}, Address: {address}, Rating: {rating}")
