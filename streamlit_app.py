import streamlit
import pandas
import snowflake.connector

streamlit.title("My parents new healthy diner")  
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text(" 🍞CurdRice")
streamlit.text(" 🥑 Juice")
streamlit.text("🥣 RagiMalt")
# streamlit.body("Hello")
# print("Hello")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# streamlit.dataframe(my_fruit_list)
# Display the table on the page.

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response.json())
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruiturl = "https://fruityvice.com/api/fruit/"+fruit_choice

fruityvice_selectedresponse = requests.get(fruiturl)

fruityvice_selectedresponse_normalized = pandas.json_normalize(fruityvice_selectedresponse.json())
streamlit.dataframe(fruityvice_selectedresponse_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list containts ")
streamlit.dataframe(my_data_rows)

streamlit.text("")
fruits_added=streamlit.text_input("What fruit you would like to add ",
        "Add Fruit",
        key="placeholder",)
streamlit.text("Thanks for adding ",fruits_added)


