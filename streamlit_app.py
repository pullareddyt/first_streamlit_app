
import streamlit
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.title('My parents new healthy diner')
streamlit.text('i want to eat pizza')
streamlit.header('🐔 Breakfast Menu')
streamlit.text(' 🥑 Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('🥣 🥗 🐔 🥑🍞 Hard-Boiled Free-Range Egg')

iport pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
