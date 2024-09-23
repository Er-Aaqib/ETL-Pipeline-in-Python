# Python ETL Pipeline: From Weather API to Data Insights
Creating a ETL pipeline in Python to retrieve weather data from an API, transform the data, and save it to a CSV file.

**1. Project Introduction**

This project, "Python ETL Pipeline: From Weather API to Data Insights", is designed as a guide to demonstrate how to construct an Extract, Transform, Load (ETL) pipeline using Python. ETL pipelines are crucial in data engineering and analytics to extract data from various sources, transform it into the desired format, and load it into target systems for analysis or further processing. This project focuses on fetching weather data from an external API using Python, processing it, and loading it for further analysis.

**2. Objective**

The key objective of this project is to provide a clear and concise guide for building an ETL pipeline using Python. The pipeline performs the following functions:

- Extracts weather data from a public API (OpenWeatherMap).
- Transforms the data by processing and structuring it in a usable format.
- Loads the transformed data into a target system for analysis or storage.

**3. Technologies Used**
- Programming Language: Python
- IDE: VS Code
- API: OpenWeatherMap API ([OpenWeather API](https://home.openweathermap.org/api_keys))
- Libraries:
  - requests: for making HTTP requests to the weather API.
  - json: for parsing the JSON responses from the API.
  - pandas: for data manipulation and transformation.

**4. Project Overview**

 This ETL pipeline comprises three distinct modules, each designed to fetch weather data through different parameters from the OpenWeatherMap API.

**4.1. ETL Pipeline Overview**
 
 The pipeline follows the basic steps of extracting data from an external source, transforming it, and loading it into a specified destination. The transformation stage includes parsing the JSON data, filtering relevant information such as temperature, humidity, and weather conditions, and structuring it into a suitable format. After the transformation, the data is saved as a CSV file for further analysis or storage.

**4.2. Data Sources and Transformation Process**
 
 The data source for this project is the OpenWeatherMap API, which provides real-time weather data. The extraction involves fetching the data from the API using different input parameters (city name, city ID, and ZIP code), followed by data transformation where the raw JSON data is filtered and organized. The transformed data is then saved as a CSV file, providing a structured format for easy access and further processing.

**4.3. Key Modules**

- **Fetch Weather Data by City Name:**
  - In this module, the pipeline takes the city name as an input parameter, sends a request to the OpenWeatherMap API, and retrieves the weather data for that city [Built-in API request by city name](https://openweathermap.org/current#name)).

- **Fetch Weather Data by City ID:**
  - This module takes the unique city ID as the input parameter and returns the weather data for the corresponding city ([Built-in API request by city ID](https://openweathermap.org/current#cityid))

- **Fetch Weather Data by ZIP Code:**
  - In this module, the pipeline uses a ZIP code to request weather data for the region associated with the code. The API response is then parsed, and relevant weather data is extracted [Built-in API request by ZIP code](https://openweathermap.org/current#zip)).

**4.4. Python Code Implementation**

 In this project, the ETL process involves three main stages: extraction of weather data, transformation of the extracted data, and loading the transformed data into a CSV file. Below is the code implementation for each of these stages, along with a detailed explanation of how the city name and file-saving destination are changed dynamically.

 **1. Fetching Weather Data by City Name**

  *The fetch_weather_data function is responsible for extracting weather data from the OpenWeatherMap API by passing the city name as a parameter. The API key is also included in the request for authentication.*

```
import requests
import pandas as pd

def fetch_weather_data (city: str, api_key: str):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

api_key = '6d52ac0fcbf0e5873b3c5a3c5f2d8583'
city = 'los angeles'
weather_data = fetch_weather_data(city, api_key)

print(weather_data) 
```

   ***Explanation:***

  - The city parameter allows the user to change the city dynamically for which the weather data is being fetched.
  - The api_key is necessary to authenticate requests with the OpenWeatherMap API.
  - The API responds with JSON data, which is used in the next step of transformation.


 **2. Transforming Weather Data**

  *The transform_weather_data function processes the raw JSON data fetched from the API, extracting relevant fields like temperature, humidity, weather description, and wind information.*

```
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

transformed_data = transform_weather_data(weather_data)

print(transformed_data)
```
  ***Explanation:***

- This function extracts and organizes the data into a structured dictionary format (weather_info) to be saved into a CSV file.
- You can now see a simplified view of the weather data, which is ready for further use.


 **3. Loading Data to CSV**

  *The load_data_to_csv function saves the transformed data into a CSV file. The destination path and file name are passed dynamically.*

```
def load_data_to_csv(data: dict, file_path: str):
    df = pd.DataFrame([data])
    df.to_csv(file_path, index=False)

output_file = '/users/aaqibkhan/python/weather_data/fetch_weather_cityname_LA.csv'
load_data_to_csv(transformed_data, output_file)


print(f'Data saved to {output_file}')
```
***Explanation:***

- The file_path parameter allows the user to specify the desired location and file name for saving the CSV file. In the example, the weather data for Los Angeles is saved to a CSV file with the name fetch_weather_cityname_LA.csv.
- The file-saving destination (output_file) can be changed by modifying the file_path to any valid file path on your system, and the file name can be customized to reflect the city or other identifying information.






**5. Challenges Faced**

- **Handling API Rate Limits:**
During development, managing the API's rate-limiting feature was a challenge, as it restricted the number of API requests made in a given period.

- **Data Transformation:**
Structuring the API's JSON response into a format suitable for analysis required careful parsing and manipulation of the data.

**6. Conclusion**

This project successfully demonstrates the construction of a simple ETL pipeline using Python. It highlights the process of extracting data from an API, transforming the raw data into usable formats, and loading it for further use. The modular approach allows users to extend and modify the pipeline to work with other APIs or data sources.

**7. Future Enhancements**

Possible future improvements to this project include:

- **Database Integration:** Incorporating a database system like MySQL or PostgreSQL to store the transformed data for large-scale analytics.

- **Automation:** Automating the ETL pipeline to run at scheduled intervals using tools like Apache Airflow or Cron jobs.

- **Visualization:** Adding a data visualization module to generate insights from the fetched weather data, such as temperature trends over time.

** ETL Pipeline Overview**

The following is a visual representation of the ETL (Extract, Transform, Load) pipeline for weather data using Python and the OpenWeatherMap API.


![Pipeline](https://github.com/user-attachments/assets/271628a6-cde5-4c27-9d38-a10059ca7223)


