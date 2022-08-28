#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: April 7, 2022
#This program that asks the user for the name of a CSV file, name of the output file, and creates a map with markers for all the traffic collisions from the input file

import folium
import pandas as pd

file = input('Enter a file name: ')
output = input('Enter output file name: ')

df = pd.read_csv(file)
mapNYC = folium.Map(location=[40.768731, -73.964915])

for index,row in df.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["TIME"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapNYC)

mapNYC.save(output)
    
