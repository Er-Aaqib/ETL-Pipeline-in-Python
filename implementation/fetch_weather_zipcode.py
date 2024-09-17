
#Note: can use any zip code from the US Only. 

import requests
import pandas as pd

def fetch_weather_data (zip_code : str, api_key: str):
    url = f'https://api.openweathermap.org/data/2.5/weather?zip={zip_code}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

#Example usage
api_key = '6d52ac0fcbf0e5873b3c5a3c5f2d8583'
zip_code = '99501'
weather_data = fetch_weather_data(zip_code, api_key)
# print(weather_data)


def transform_weather_data(data: dict):
    if not data:
        return None

    weather_info = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'weather': data['weather'][0]['description'],
        'wind_speed': data['wind']['speed'],
        'wind_deg': data['wind']['deg']
    }
    return weather_info

# Example usage
transformed_data = transform_weather_data(weather_data)
# print(transformed_data)

def load_data_to_csv(data: dict, file_path: str):
    df = pd.DataFrame([data])
    df.to_csv(file_path, index=False)

# Example usages
output_file = '/users/aaqibkhan/python/weather_data/fetch_weather_zipcode_99501.csv'
load_data_to_csv(transformed_data, output_file)
print(f'Data saved to {output_file}')

