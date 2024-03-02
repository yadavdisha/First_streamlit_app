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
def get_fruit(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
   
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
        streamlit.error("please select fruit to get info")
   else:
      back_from_function=get_fruit( fruit_choice )
      streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()


def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
        return my_cur.fetchall()
if streamlit.button('Get fruit load list'):
     
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     my_data_row=get_fruit_load_list()
     streamlit.dataframe(my_data_row)
                     


def insert_into_snowflake(new_fruit):
     with my_cnx.cursor() as my_cur:
         my_cur.excute("insert into fruit_load_list values('from streamlit')")
         return "Thanks for adding"+new_fruit

add_my_fruit=streamlit.text_input('What fruit you would like to add')
if streamlit.button('Add fruit to list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function=insert_into_snowflake( add_my_fruit)
    streamlit.text( back_from_function)


    
              


