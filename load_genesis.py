from genesis import genesis
import streamlit as st

def load(name):
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

