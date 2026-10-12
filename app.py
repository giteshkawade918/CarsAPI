import streamlit as st
import pandas as pd
from fetch_data import get_cars
st.title("Car Rental Dashboard")
df = get_cars()
st.write("Total Cars")
st.metric("Total Cars",len(df))


#Add search functionality
search=st.text_input("Search by Brand")
if search:
    df[df["brand"].str.contains(search,case=False)]
    st.dataframe(df)


#Add filter functionality
multiselect=st.multiselect("Select Brands",df["brand"].unique())
if multiselect:
    df=df[df["brand"].isin(multiselect)]
st.dataframe(df)

#Add Chart functionality
st.bar_chart(df.groupby('brand').size())


