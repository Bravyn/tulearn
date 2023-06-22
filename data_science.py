import streamlit as st
import requests
from genesis import genesis
from user_data import save_user, user_name, user_passkey, user_password
global exp

users = []
import time

#st.header("THE MASTERMIND")
#st.caption("Created by Ian Bravyn (ianbravynsa@gmail.com)")
  

def start_engine():
    st.title("Data Science Detective Engine Running")
    st.caption("Running on ALIEN DNA")
    name = user_name()  
    password = user_password()
    passkey = user_passkey(password)

    save_user(name, passkey, users)

    exp = 10
    col1, col2 = st.columns([3, 1])
    #name = st.text_input("What is your name, detective?")
    if name:
        with col1:
            exp = genesis(exp, name)
            
        with col2:
            bar = st.progress(0, f"Detective {name}'s Experience")
            bar.progress(exp,f"Detective {name}'s Experience" )
            #st.success(f"Experience Points: {exp}pts.")
    else:
        st.warning("PLease enter name")


txt = "Loading State"


def start(): 
    bar = st.progress(0, txt)
    
    for i in range(100):
        bar.progress(i, f":blue[{txt}]" )
        time.sleep(.0318)

    start_engine()  

