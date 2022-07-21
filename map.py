


#importing required libraries

import streamlit as st
import pandas as pd
import numpy as np





#creating a sample data consisting different points 
df = pd.DataFrame(np.random.randn(800, 2) / [50, 50] + [46.34, -108.7],columns=['latitude', 'longitude'])
st.write(df)

#plotting a map with the above defined points
st.map(df)


# import leafmap.foliumap as leafmap
# m = leafmap.Map()
# data = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
# m.add_points_from_xy(data)
# m
