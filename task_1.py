import requests
import matplotlib.pyplot as plt


API_KEY = "f98926e3aaaee1dc539bcb07d5552a17"
CITY = "Visakhapatnam"
URL = "https://api.openweathermap.org/data/2.5/weather?q=Visakhapatnam&appid=f98926e3aaaee1dc539bcb07d5552a17&units=metric"

response = requests.get(URL)
data = response.json()

temperature = data['main']['temp']
humidity = data['main']['humidity']
pressure = data['main']['pressure']

labels = ['Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)']
values = [temperature, humidity, pressure]

plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=['orange', 'skyblue', 'lightgreen'])
plt.title(f"Weather Data for {CITY}")
plt.ylabel("Values")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
