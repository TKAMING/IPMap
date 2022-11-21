# by Tobias Karuth (TKAMING)

import folium
import requests
from flask import Flask, render_template, redirect, request

# gets ip cordinates
def ip_cordinates():
    response = requests.get("http://ip-api.com/json/" + ip).json()

    global lat
    lat = response['lat']
    global lon
    lon = response['lon']

# makes map
def built_map():
    map = folium.Map(zoom_start=12, control_scale=True)
    folium.CircleMarker([lat, lon], radius=50, popup="The radius the IP could be in").add_to(map)
    folium.Marker([lat, lon], popup='The IP you searched for', icon=folium.Icon(color="black")).add_to(map)

    # save and display the map
    map.save('templates/map.html')

# flask processes
app = Flask(__name__)

#  ---------------------------------    USERFORM PAGE    -----------------------------------

@app.route("/", methods=["GET", "POST"])
def index():
    ()
    if request.method == "POST":
        global ip
        ip = request.form.get("ip")
        if ip == "":
            return redirect("/")
        else:
            return redirect("/map") 

    else:
        return render_template("index.html")

#  ---------------------------------    MAP PAGE    -----------------------------------

@app.route("/map")
def map():
    if request.method == "GET":
        built_map()
        return render_template("map.html")

if __name__ == "__main__":
    app.run(debug=True)