import pandas
import streamlit
streamlit.title("My Mom's New Healthy Dinner")
streamlit.header('🍞Breakfast Menu')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🥣Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑Avacado Toast')
fruit_list=pd.read.csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
stramlit.dataframe(fruit_list)
   
