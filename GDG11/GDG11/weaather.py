import requests
API_KEY = 'fe18bb89ada0136c321ed2ba37a38acb'
city = input("City name bro: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if str(data.get('cod')) == "200":
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    print(f"\nWeather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {description.capitalize()}")
else:
    print(f"\nError: {data.get('message', 'write the existing city bruh')}")