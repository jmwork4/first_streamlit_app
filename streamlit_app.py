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

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
