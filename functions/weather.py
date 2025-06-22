import requests

API_KEY = "33f3b98c8f4541a8aff113319251506"
city = "Mukono"  # or any city you want
url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

response = requests.get(url)
weather_data = response.json()

# Extract and print weather info
print(f"Temperature: {weather_data['current']['temp_c']}°C")
print(f"Condition: {weather_data['current']['condition']['text']}")