import streamlit as st
import time

def cards(content):
    st.markdown(f"""
    <style>
        .card{{
              background: rgba(205, 255, 255, .5) ;
              -webkit-backdrop-filter:blur(.3rem);
              backdrop-filter: blur(.3rem);
              font-size: 1rem;
              border: 4px solid rgba(255, 255, 255, .9);
              padding: .7rem;
              border-radius: 1rem;
          }}
       
    </style>
    
    """, unsafe_allow_html=True)
    for card in content:
        st.markdown(f'<div class = "card"> {card}</div>', unsafe_allow_html=True)


with open("mastermind.txt", 'r') as f:
    data = f.read()
    data = data.split(".")

    cards(data)
        

       
        
