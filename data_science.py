import streamlit as st
import hashlib
users = []

def password():
    password = st.text_input("Type in your password", type='password')
    return password

def passkey(password):
    sha256hash = hashlib.sha256()
    sha256hash.update(password.encode('utf-8'))
    hash_key = sha256hash.hexdigest()
    return hash_key

def name():
    name = st.text_input("Put in your fucking username you idiot")
    if name:
        st.write(f"For f*cks sake who named you **{name.capitalize()},** dude?")
        st.write(":blue[Fu*king get out of here!!!]")
 
        st.caption("Just kidding, chill the fuck out:sunglasses:")
    return name

def save_user(name, passkey, userDB):
    user = f"{ name } :{ passkey }"
    if user not in userDB:
        userDB.append(user)  


def start_engine(key):
    st.title("Booting Up The DS Engine")
    st.caption("Running on ALIEN DNA")
    
password = password()
passkey = passkey(password)
name = name()
save_user(name, passkey, users)




