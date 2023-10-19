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


