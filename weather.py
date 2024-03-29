import requests

'''By typing the city name, you will get the latest weather information
'''

API_KEY = '2366a9a78c487f57a277ae2b0d401128'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

city = input('Enter the City name: ')
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15)
    print("Weather: ", weather)
    print("Temperature: ", temperature, "celsius")
else:
    print("Error")
