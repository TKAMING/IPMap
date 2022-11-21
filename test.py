import folium
import geocoder

g = geocoder.ipinfo('199.7.157.0')
ip_cordinates = g.latlng

print(g.latlng)
