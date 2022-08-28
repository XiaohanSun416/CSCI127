#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: April 7, 2022
#This program that uses folium to make a map of New York City

import folium
import pandas as pd

mapCUNY = folium.Map(location=[40.75, -74.125])
folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapCUNY)

mapCUNY.save(outfile='nycMap.html')
