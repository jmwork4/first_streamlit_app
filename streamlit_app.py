import streamlit
streamlit.title ('My Parents New Healthy Diner')
streamlit.header ('Breakfast Menu')

menu_items = [
    'Omega 3 & Blueberry Oatmeal',
    'Kale, Spinach & Rocket Smoothie',
    'Hard-Boiled Free Range Egg'
]

for item in menu_items:
    streamlit.write(item)





