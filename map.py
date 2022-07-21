


#importing required libraries

import streamlit as st

import pandas as pd

import numpy as np



#simply plotting a map with no parameters

st.map()



#creating a sample data consisting different points 

df = pd.DataFrame(np.random.randn(800, 2) / [50, 50] + [46.34, -108.7],columns=['latitude', 'longitude'])



#plotting a map with the above defined points

st.map(df)
