import streamlit as st
st.title('Interactive Streamlit App")
name=st.text_input('Enter your name")
if st.button("submit"):
                   st.write(f"Hello, {name}! Welcome to Streamlit.")
