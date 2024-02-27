import pandas as pd
import streamlit
streamlit.title("My Mom's New Healthy Dinner")
streamlit.header('🍞Breakfast Menu')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🥣Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑Avacado Toast')
fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list=fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some food:" ,list(fruit_list.index))
streamlit.dataframe(fruit_list)
   
