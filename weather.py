import requests
import json

# API key for OpenWeatherMap
api_key = 'dd78c30cb384d116fa9452da1e35f309'

# Get the current weather
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}'
    response = requests.get(url)
    weather_data = json.loads(response.text)
    return weather_data

# Generate a quote based on the weather
def generate_quote(weather_data):
    weather_id = weather_data['weather'][0]['id']
    if weather_id >= 200 and weather_id < 300:
        return "It's a stormy day. Stay safe and dry."
    elif weather_id >= 300 and weather_id < 600:
        return "It's a rainy day. Don't forget your umbrella."
    elif weather_id >= 600 and weather_id < 700:
        return "It's a snowy day. Wrap up warm and enjoy the winter wonderland."
    elif weather_id >= 700 and weather_id < 800:
        return "It's a misty or foggy day. Take care on the roads."
    elif weather_id == 800:
        return "It's a clear day. Enjoy the sunshine."
    elif weather_id >= 801 and weather_id < 900:
        return "It's a cloudy day. Perfect for a walk in the park."
    else:
        return "I'm sorry, I don't know the weather."

# Ask user for city name
city = input("Enter the city name: ")

# Print the current weather and quote
weather_data = get_weather(city)
print(f'Weather for {city}: {weather_data["weather"][0]["main"]}')
print(generate_quote(weather_data))