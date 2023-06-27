import hashlib
import streamlit as st

def user_password():
    password = st.text_input("Type in your password", type='password')
    if not password:
        st.warning("A detective MUST be secure")
    return password

def user_passkey(password):
    sha256hash = hashlib.sha256()
    sha256hash.update(password.encode('utf-8'))
    hash_key = sha256hash.hexdigest()
    return hash_key

def user_name():
    name = st.text_input("Type in your name please:")
    if not name:
        st.warning("A good data detective needs a name!")
        return
    else:
        st.caption(f"Nice to meet you {name.capitalize()}, I, am The Mastermind :sunglasses:")
    return name

def save_user(name, passkey, userDB):
    user = dict({name, passkey})
    if user not in userDB:
        userDB.append(user)