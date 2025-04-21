import requests
API_KEY = 'fe18bb89ada0136c321ed2ba37a38acb'
city = input("City name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()
if data.get('cod') == 200:
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    print(f"\nTemperature in the city {city}: {temp}°C")
    print(f"Weather: {description}")
else:
    print("Write the existing city bruh")