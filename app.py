# by Tobias Karuth (TKAMING)

import folium
import geocoder
from flask import Flask, render_template, redirect, request

# makes map
def built_map():
    g = geocoder.ipinfo(form_ip)
    userip = g.latlng
    if userip == []:
        print("[*] Error IP cordinates not found" + form_ip)
        userip = [43.7001, -79.4163]

    map = folium.Map(location=userip, zoom_start=12, control_scale=True)
    folium.CircleMarker(location=userip, radius=50, popup="The radius the IP could be in", circle=folium.Circle(color="black")).add_to(map)
    folium.Marker(userip, popup='The IP you searched for', icon=folium.Icon(color="black")).add_to(map)

    # save and display the map
    map.save('templates/map.html')


# flask processes
app = Flask(__name__)

#  ---------------------------------    USERFORM PAGE    -----------------------------------

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        global form_ip
        form_ip = request.form.get("ip")

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