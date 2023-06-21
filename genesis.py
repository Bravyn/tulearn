import streamlit as st

def genesis(name= "zainab"):
    if not name:
        st.write("Can't Start the Detective Data Engine without a name")
    else:
        st.caption("The Mastermind:")
        st.write(f"""Ah {name}, the weight of our investigation
        rests heavily upon us. The local police depart
        ment has sought our aid in unraveling a series
        of unsolved crimes that have struck fear into
        the heart of our city. The secrets lie hidden 
        within a mysterious dataset they have provided-
        each row a piece of the puzzle. Our task, {name},
        is to wield the power of data science to uncover
        the truth behind these heinous acts. 
        """)
    st.divider()
    st.write(f"What shall we do {name} ? ")
