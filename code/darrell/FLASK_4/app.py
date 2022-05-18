
from flask import Flask, render_template, request
import requests
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template('home.html')
    elif request.method == "POST":
        street = request.form['street']
        city = request.form['city']
        state = request.form['state']
        response = requests.get(
            f"https://maps.googleapis.com/maps/api/geocode/json?address={street},{city},{state}&key=AIzaSyCamJWA17Tsl2xJJLlb1BvFlPWmpjh0Xew")
        data = response.json()
        results = data['results']
        dict = results[0]
        address = dict['address_components']
        street_num = address[0]
        street_num = street_num['long_name']
        street = address[1]
        street = street['long_name']
        city = address[3]
        city = city['long_name']
        county = address[4]
        county = county['long_name']
        state = address[5]
        state = state['short_name']
        zip = address[7]
        zip = zip['long_name']
        geometry = dict['geometry']
        location = geometry['location']
        lat = location['lat']
        long = location['lng']
        print(results)
        print(f"{street_num} {street} {city} {county} {state} {zip}")
        print(lat)
        print(long)
        return render_template('map.html', data=data, lat=lat, long=long, street_num=street_num, street=street, city=city, county=county, state=state, zip=zip)


@app.route('/map/', methods=["GET", "POST"])
def map():
    return render_template('map.html')


app.run(debug=True)
