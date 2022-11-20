# by Tobias Karuth (TKAMING)

import folium
import geocoder
from flask import Flask, render_template, redirect, request

# makes map
def built_map(form_ip):
    userip = FindIp(form_ip)
    map = folium.Map(zoom_start=12,control_scale=True, width='100%', height='80%')
    map_circle(userip)

    # save and display the map
    map.save('templates/map.html')

# makes the circle
def map_circle(userip):
    folium.CircleMarker(location=userip, radius=50, popup="The IP you searched for").add_to(map)

    # save and display the map
    map.save('templates/map.html')


# get the ip and find cordinates
def FindIp(ip):
    g = geocoder.ip(ip)
    ip_cordinates = g.latlng
    return ip_cordinates


# flask processes
app = Flask(__name__)

#  ---------------------------------    USERFORM PAGE    -----------------------------------

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form_ip = request.form.get("ip")
        return form_ip, redirect("/map") 

    else:
        return render_template("index.html")

#  ---------------------------------    MAP PAGE    -----------------------------------

@app.route("/map")
def map(form_ip):
    built_map(form_ip)
    return render_template("map.html")


if __name__ == "__main__":
    app.run(debug=True)