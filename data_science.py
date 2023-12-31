import streamlit as st
import requests
from user_data import save_user, user_name, user_passkey, user_password
global exp
from load_genesis import load, unload

users = []
import time

#st.header("THE MASTERMIND")
#st.caption("Created by Ian Bravyn (ianbravynsa@gmail.com)")
  

def start_engine():
    st.title(":red[Data Science Detective Engine Running:sunglasses:]")
    st.caption("Running on ALIEN DNA:alien:")
    name = user_name()  
    password = user_password()
    passkey = user_passkey(password)

    save_user(name, passkey, users)

    
#txt = "Loading State"
def start(): 
    #bar = st.progress(0, txt)
  
    #for i in range(100):
        #bar.progress(i, f":blue[{txt}]" )
        #time.sleep(.07)

    start_engine()

def load_gen(users = users):
    if len(users) > 0:
        load(users[-1]['name'])

def unload_gen(users = users ):
    unload(users)
    #pass

