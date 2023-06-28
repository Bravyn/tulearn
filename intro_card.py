import streamlit as st

def cards(content):
    st.markdown("""<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,100;0,200;0,300;0,400;0,500;0,700;1,100;1,200&display=swap" rel="stylesheet">""", unsafe_allow_html=True)
    st.markdown(f"""
    <style>
        .card{{
              background: #333333;
              color: #fff; 
              font-family: 'Kanit', sans-serif;
              -webkit-backdrop-filter:blur(.3rem);
              backdrop-filter: blur(.3rem);
              font-size: 1rem;
              border: 4px solid rgba(255, 255, 255, .9);
              padding: .9rem;
              border-radius: 1rem; 
              margin: 0 auto;
          }}
        .card:hover{{
                transform: translate(.5rem, .5rem)
        }}
       
    </style>
    
    """, unsafe_allow_html=True)
    for card in content:
        if card != content[-1]:
            st.markdown(f'<div class = "card"> { card  + "." }</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class = "card"> { card }</div>', unsafe_allow_html=True)
