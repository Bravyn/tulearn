import streamlit as st

def start_engine(key):
    st.title("Booting Up Engine")
    st.caption("Running on ALIEN DNA")
    name = st.text_input("Put in your fucking username you idiot")
    if name:
        st.write(f"For fucks sake who named you: {name}")
        st.write("Fuking get out of here!!!")
        st.caption("Just kidding, chill the fuck out")

start_engine()