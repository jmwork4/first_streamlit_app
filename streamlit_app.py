#Created streamlit py file
#import streamlit and pandas
import streamlit
import pandas
streamlit.title ('My Parents New Healthy Diner')
streamlit.header ('Breakfast Favorites')

menu_items = [
'🥣 Omega 3 & Blueberry Oatmeal',
'🥗 Kale, Spinach & Rocket Smoothie',
'🐔 Hard-Boiled Free Range Egg',
'🥑🍞 Avocado Toast'
    
]

for item in menu_items:
    streamlit.write(item)

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Let's put a pick list here so they can pick the fruit they want to include
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])

#display the table on the page
#streamlit.dataframe(my_fruit_list)

#display the table on the page
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
#streamlit.text(fruityvice_response.json()) #just writes the data to the screen


# normalize and store data -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# displays the normalized data - what does this do?
streamlit.dataframe(fruityvice_normalized)

#import snowflake connector
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

#adding text entry to add fruit to list
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thank you for entering ', add_my_fruit)
