import folium
from folium.plugins import *
import pandas as pd

# main code, makes map
def main():

    # generate map
    map = folium.Map(zoom_start=12, control_scale=True, width='100%', height='80%', attr='CosmodiumCS Theme')
    # feature group
    fg = folium.FeatureGroup().add_to(map)
    map.add_child(fg)
 
    # plugins
    minimap = MiniMap()
    map.add_child(minimap) # mini map
    LocateControl(auto_start=True).add_to(map) # user location
    Fullscreen().add_to(map) # full screen
    MousePosition().add_to(map) # mouse position coordinates
    folium.features.ClickForMarker().add_to(map) # click for marker
    Geocoder().add_to(map) # search bar
    FloatImage(image='https://static.wixstatic.com/media/1a48ab_c140d7ec1edc4c44aeb9bca9ce00cc3e~mv2.png/v1/fill/w_50,h_50,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/1a48ab_c140d7ec1edc4c44aeb9bca9ce00cc3e~mv2.png', bottom=23, left=0).add_to(map) # floating logo

    # themes
    folium.TileLayer('openstreetmap').add_to(map)
    folium.TileLayer('cartodbdark_matter').add_to(map)
    folium.TileLayer('cartodbpositron').add_to(map)
    folium.TileLayer('stamentoner').add_to(map)
    folium.LayerControl().add_to(map)

if __name__ == "__main__":
    main()