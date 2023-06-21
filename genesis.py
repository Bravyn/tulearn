import streamlit as st

def genesis(experience, name= "zainab"):
    if not name:
        st.write("Can't Start the Detective Data Engine without a name")
    else:
        st.caption("The Mastermind:")
        st.write(f"""Ah {name}, the weight of our investigation
        rests heavily upon us. The local police depart
        ment has sought our aid in unraveling a series
        of unsolved crimes that have :red[struck fear] into
        the heart of our city. The secrets lie hidden 
        within a mysterious dataset they have provided-
        each row a piece of the puzzle. Our task, {name},
        is to wield the power of data science to uncover
        the truth behind these heinous acts. 
        """)
    st.divider()
    st.write(f":blue[What shall we do {name}] ? ")
    
    if st.button("Proceed with our analysis"):
        experience += 1
        "Proceeding"
    if st.button("I wanna quit, Mastermind"):
        experience -= 1
    return experience