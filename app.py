# by Tobias Karuth (TKAMING)

import folium
import geocoder
from flask import Flask, render_template, redirect, request

# makes map
#def main(form_ip):
#    userip = FindIp(form_ip)
#    map = folium.Map(location=userip, zoom_start=12,control_scale=True, width='100%', height='80%')
#    folium.CircleMarker(location=userip, radius=50, popup="The IP you searched for").add_to(map)
#
#    # save and display the map
#    map.save('templates/map.html')

# get the ip and find cordinates
def FindIp(ip):
    g = geocoder.ip(ip)
    ip_cordinates = g.latlng
    return ip_cordinates

# flask processes
app = Flask(__name__)

#  ---------------------------------    USERFORM PAGE    -----------------------------------

# render home page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form_ip = request.form.get("ip")
        userip = FindIp(form_ip)
        map = folium.Map(location=userip, zoom_start=12,control_scale=True, width='100%', height='80%')
        folium.CircleMarker(location=userip, radius=50, popup="The IP you searched for").add_to(map)

        # save and display the map
        map.save('templates/map.html')

        return render_template("map.html") 

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)