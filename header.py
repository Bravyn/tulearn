import streamlit as st
st.markdown("""<link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,100;0,200;0,300;0,400;0,500;0,700;1,100;1,200&display=swap" rel="stylesheet">""", unsafe_allow_html=True)
def header():

    st.markdown(f"""
    <style>
       .glitch-wrapper{{
           width: 100%;
           height: 100%
           display: flex;
           align-items: center;
           justify-content: center;
           text-align: center;
           background-color: #222;
           color: #fff;
           
           }}
        .glitch{{
            position: relative;
            font-family: 'Kanit', sans-serif;
            font-size: 2rem;
            font-weight: 700;
            line-height: 1.2;
            letter-spacing: .618rem;
            z-index: 1;

            }}
       
    <style>
    
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class = "glitch-wrapper">
                
           <div class = "glitch">
                THE MASTERMIND
            </div>
           
        </div> 
           
    """, unsafe_allow_html=True)
    st.divider()
    st.caption(":blue[Created by Ian Bravyn.]")