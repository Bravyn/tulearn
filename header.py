import streamlit as st

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
            font-size: 2rem;
            font-weight: 700;
            line-height:1.2;
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
    st.caption(":blue[**Created by Ian Bravyn.**]")