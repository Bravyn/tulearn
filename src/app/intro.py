import streamlit as st

def readmsg():
    with open("msg.txt", 'r') as f:
        st.write(f.read())

st.title("Chat Y")   
readmsg()
if st.button("Refresh"):
    readmsg()   

