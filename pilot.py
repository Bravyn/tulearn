import streamlit as st
from header import header
from data_science import start
from intro_card import cards
from data_science import load_gen


with open("mastermind.txt", 'r') as f:
    data = f.read()
    data = data.split(".")
    header()
    cards(data)
    st.divider()
    with st.expander("Get Started"):
        start()
from data_science import users
users.clear()
load_gen()

       
        
