import folium
import pandas as pd

world = folium.Map(
    zoom_start=2,
    location=[13.133932434766733, 16.103938729508073])
world

world.save('templates/index.html')
#hello
print("hello world")