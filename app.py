from flask import Flask, render_template
import requests

app = Flask(__name__)

#locations from assignment
locations = [
    {"name": "Lake District National Park", "lat": 54.4609, "lon": -3.0886},
    {"name": "Corfe Castle", "lat": 50.6395, "lon": -2.0566},
    {"name": "The Cotswolds", "lat": 51.8330, "lon": -1.8433},
    {"name": "Cambridge", "lat": 52.2053, "lon": 0.1218},
    {"name": "Bristol", "lat": 51.4545, "lon": -2.5879},
    {"name": "Oxford", "lat": 51.7520, "lon": -1.2577},
    {"name": "Norwich", "lat": 52.6309, "lon": 1.2974},
    {"name": "Stonehenge", "lat": 51.1789, "lon": -1.8262},
    {"name": "Watergate Bay", "lat": 50.4429, "lon": -5.0553},
    {"name": "Birmingham", "lat": 52.4862, "lon": -1.8904}
]

@app.route('/')
def index():
    weather_data = []
    for location in locations:
        lat, lon = location['lat'], location['lon']
        #api from openweather
        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=42c10c6eeff25fdb9a2e1ae45c758f7f&units=metric" 

        response = requests.get(api_url)
        if response.status_code == 200:
            current_weather = response.json()
            weather_data.append({
                'location': location['name'], #format
                'temperature': current_weather['main']['temp'],
                'condition': current_weather['weather'][0]['description'] #/format
            })
        else:
            #if API fails
            print(f"Failed to get data for {location['name']}")

    return render_template('index.html', weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)