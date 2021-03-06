# -*- coding: utf-8 -*-
from app import app
from flask import render_template, request
import requests
import time

from app import socketio
from flask_socketio import send, emit

#@socketio.on('client_connected')
#def test():
#    while True:
#        print("This prints once a minute.")
#        emit('alert', 'Message from backend')
#        time.sleep(60)

def get_weather_forecast(lat, lon):
    url = 'http://forecast.weather.gov/MapClick.php'
    params = {'lat': lat, 'lon': lon, 'FcstType': 'json'}
    r = requests.get(url, params=params)
    weather = r.json()
    return weather

@app.route('/alert', methods = ['POST'])
def new_weather():
    socketio.emit('alert',request.get_json(force=True).get("alert","Nothing new"))
    return "Thanks."

@app.route('/')
def index():
    weather = get_weather_forecast(35.775259, -78.637751)

    return render_template('index.html', weather=weather)
