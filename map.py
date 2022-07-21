


#importing required libraries

import streamlit as st
import pandas as pd
import numpy as np

st.header("Terraform Maps")
# 33.662855, 73.087393
# 33.66284908863495, 73.08752503127836
# 33.66292499311975, 73.08721389523399
# 33.64828985670207, 73.0941454819751
# 33.67654750697799, 73.09155556511915
# 33.68456424164071, 73.08831116090731
# 33.748218539091035, 73.07893455948549
# 33.747455517702065, 73.07445495271938
# 33.75165354102952, 73.0899628519445
# 33.59475182130361, 73.35155103293881
# 33.42437415195493, 72.92496925817787


lat=[
33.662855, 
33.66284908863495, 
33.66292499311975, 
33.64828985670207, 
33.67654750697799, 
33.68456424164071,
33.748218539091035, 
33.747455517702065,  
33.75165354102952, 
33.59475182130361,  
33.42437415195493,  
]

lon=[
  73.087393, 
  73.08752503127836, 
  73.08721389523399, 
  73.094145481975, 
  73.09155556511915,
  73.08831116090731,
  73.0789345594854, 
  73.07445495271938,
  73.089962851944,
  73.351551032938,
  72.92496925817787,
]

#creating a sample data consisting different points 
# df = pd.DataFrame(np.random.randn(800, 2) / [50, 50] + [46.34, -108.7],columns=['latitude', 'longitude'])
# df = pd.DataFrame(np.random.randn(800, 2) / [50, 50] + [46.34, -108.7] , columns=['latitude', 'longitude'])

df = pd.DataFrame({'latitude': lat,'longitude': lon} , columns=['latitude', 'longitude']) 
#st.write(df)




#plotting a map with the above defined points
st.map(df)


# import leafmap.foliumap as leafmap
# m = leafmap.Map()
# data = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
# m.add_points_from_xy(data)
# m
