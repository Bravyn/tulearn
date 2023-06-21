import streamlit as st
import hashlib
import requests

users = []
import time

def password():
    password = st.text_input("Type in your password", type='password')
    return password

def passkey(password):
    sha256hash = hashlib.sha256()
    sha256hash.update(password.encode('utf-8'))
    hash_key = sha256hash.hexdigest()
    return hash_key

def name():
    name = st.text_input("Put in your fucking name you idiot")
    if name:
        st.caption(f"Nice to meet you {name.capitalize()}, I, am The Mastermind :sunglasses:")
    return name

def save_user(name, passkey, userDB):
    user = f"{ name } :{ passkey }"
    if user not in userDB:
        userDB.append(user)  

def start_engine():
    st.title("Booting Up The DS Engine")
    st.caption("Running on ALIEN DNA")
    
password = password()
passkey = passkey(password)
name = name()
save_user(name, passkey, users)

txt = "Loading State"

if st.button("Let me in!"):
    bar = st.progress(0, txt)
    
    for i in range(100):
        bar.progress(i, f":blue[{txt}]" )
        time.sleep(.0318)
    start_engine()  


col1, col2 = st.columns(2)

with col1:
    genesis(name)
with col2:
    st.info("col2")

