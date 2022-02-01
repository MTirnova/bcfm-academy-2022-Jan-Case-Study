from flask import Flask, jsonify,request
import requests
import json
import config
app=Flask(__name__)
@app.route("/")
def index():
    return jsonify(firstname="Mustafa",lastname="TIRNOVA"),200

@app.route("/temperature",methods=['GET'])
def temperature_api():
    city=request.args.get("city")
    base_url= requests.get(f'https://api.openweathermap.org/data/2.5/weather?q='+city+'&mode=json&lang=tr&units=metric&appid='+config.api_key)
    weatherData=base_url.json()
    temp= weatherData['main']['temp']
    return jsonify(temperature=temp),200

    

if __name__=="__main__":
    app.run(debug=True)
    