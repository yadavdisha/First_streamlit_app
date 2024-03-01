import pandas as pd
import streamlit
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My Mom's New Healthy Dinner")
streamlit.header('🍞Breakfast Menu')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🥣Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑Avacado Toast')
fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list=fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some food:" ,list(fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
        streamlit.error("please select fruit to get info")
   else:
       fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
       fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
       streamlit.dataframe(fruityvice_normalized)
except URLError as e
    streamlit.error()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("fruit list contain:")
streamlit.dataframe(my_data_rows)
add_my_fruit= streamlit.text_input('What fruit would you like information add?','Jackfruit')

streamlit.write('The user entered ', add_my_fruit)
my_cur.execute("insert into fruit_load_list values('from streamlit')")
