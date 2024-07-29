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
           background-color: #800000;
           color: #fff;
           transform: rotate(1.618deg);   
          border-radius: .3rem;   

           }}
        .glitch{{
            padding: .618rem;
            position: relative;
            font-family: 'Kanit', sans-serif;
            font-size: 2rem;
            font-weight: 100;
            line-height: 1;
            letter-spacing: .618rem;
            z-index: 1;
            }}
                
        .glitch:hover{{
            transform: rotate(-3.141deg);      

        }}
       
        
        
    <style>
    
    """, unsafe_allow_html=True)
    col1, col2 = st.columns([4,1])
    with col1:
        st.markdown(f"""
            <div class = "glitch-wrapper">
                    
            <div class = "glitch">
                    THE MASTERMIND
                </div>
            
            </div> 
            
        """, unsafe_allow_html=True)
    #st.divider()
    with col2:
        st.caption(":red[Created by :blue[Ian Bravyn].:sunglasses:]")