# by Tobias Karuth (TKAMING)

import folium
import requests
import os
import glob
from flask import Flask, render_template, redirect, request
import json

class CountCalls: 
    def __init__(self, func): 
        self._count = 0 
        self._func = func 
    def __call__( self, *args, **kwargs): 
        self._count += 1 
        return self._func(*args,**kwargs) 
    @property 
    def call_count(self): 
        return self._count

# gets ip cordinates
def ip_cordinates():
    global response
    response = requests.get("http://ip-api.com/json/" + ip).json()

    if response["status"] == "fail":
        print(f"[*] Error: Couldn´t find IP address ({ip}) location")
        return NameError
    
    else:
        global lat
        lat = response['lat']
        global lon
        lon = response['lon']

@CountCalls
# makes map
def built_map():

    if response["status"] == "fail":
        print(f"[*] Error: Couldn´t generate map (No cordinates)")
        return NameError

    else:
        map = folium.Map([lat, lon], zoom_start=12, control_scale=True)
        folium.CircleMarker([lat, lon], radius=50, popup="The radius the IP could be in").add_to(map)
        folium.Marker([lat, lon], popup='The IP you searched for', icon=folium.Icon(color="black")).add_to(map)
    
    # create new map file 
    with open(f"templates/maps/map{built_map.call_count}.html", 'w') as fp:
        # save and display the map
        map.save(f'templates/maps/map{built_map.call_count}.html')

# flask processes
app = Flask(__name__)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

#  ---------------------------------    USERFORM PAGE    -----------------------------------

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # deletes the old map
            print(f"[*] Removes old map.html files")
            all_files = glob.glob('templates/maps/*.html', recursive=True)
            for f in all_files:
                os.remove(f)
        except:
            FileExistsError
        global ip
        ip = request.form.get("ip")
        if ip == "":
            return redirect("/")
        else:
            return redirect("/map") 

    else:
        response = ""
        return render_template("index.html")

#  ---------------------------------    MAP PAGE    -----------------------------------

@app.route("/map")
def map():
    if request.method == "GET":
        try:
            if ip != NotImplemented:
                ip_cordinates()
                built_map()

                if built_map() == NameError or ip_cordinates == NameError:
                    return redirect("/")

            else:
                return redirect("/")

        except:
            NameError
            return redirect("/")
        
        try: 
            if ip == "":
                return redirect("/")

        except:
            NameError

        return render_template(f"maps/map{built_map.call_count}.html")

if __name__ == "__main__":
    app.run(debug=True)