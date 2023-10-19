import streamlit
streamlit.title ('Breakfast Favorites')
streamlit.header ('Breakfast Menu')

menu_items = [
'🥣 Omega 3 & Blueberry Oatmeal',
'🥗 Kale, Spinach & Rocket Smoothie',
'🐔 Hard-Boiled Free Range Egg',
'🥑🍞 Avocado Toast'
    
]

for item in menu_items:
    streamlit.write(item)

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)

