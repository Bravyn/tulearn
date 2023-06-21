import streamlit as st
import hashlib
import requests
from genesis import genesis

users = []
import time

def password():
    password = st.text_input("Type in your password", type='password')
    if not password:
        st.warning("A detective MUST be secure")
    return password

def passkey(password):
    sha256hash = hashlib.sha256()
    sha256hash.update(password.encode('utf-8'))
    hash_key = sha256hash.hexdigest()
    return hash_key

def name():
    name = st.text_input("Type in your name please:")
    if not name:
        st.warning("A good data detective needs a name!")
        return
    else:
        st.caption(f"Nice to meet you {name.capitalize()}, I, am The Mastermind :sunglasses:")
    return name

def save_user(name, passkey, userDB):
    user = f"{ name } :{ passkey }"
    if user not in userDB:
        userDB.append(user)  

def start_engine():
    st.title("Booting Up The DS Engine")
    st.caption("Running on ALIEN DNA")

#name = name()   
#password = password()
#passkey = passkey(password)

#save_user(name, passkey, users)

#txt = "Loading State"

#if st.button("Let me in!"):
    #bar = st.progress(0, txt)
    
    #for i in range(100):
        #bar.progress(i, f":blue[{txt}]" )
        #time.sleep(.0318)
    #start_engine()  

exp = 10
col1, col2 = st.columns([3, 1])
#name = st.text_input("What is your name, detective?")
with col1:
    genesis()
with col2:
    st.success(f"Experience Points: {exp}pts.")

