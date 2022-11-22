import folium
import geocoder
import requests

#response = requests.get("http://ip-api.com/json/" + ip).json()
#if response["status"] == "fail":
#    print(response)
#
#g = geocoder.ipinfo('199.7.157.0')
#ip_cordinates = g.latlng

# get the ip and find cordinates
#def FindIp(ip):
#    g = geocoder.ipinfo(ip)
#    ip_cordinates = g.latlng
#    return ip_cordinates