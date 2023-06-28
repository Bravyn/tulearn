import streamlit as st
from chapter_one import chapter_one    

def genesis(experience, name):
    if not name:
        st.write("Can't Start the Detective Data Engine without a name")
    else:
        name = name.capitalize()
        st.caption("The Mastermind:")
        st.write(f"""Ah {name}, the weight of our investigation
        rests heavily upon us. The local police department has sought our aid in unraveling a series
        of unsolved crimes that have :red[struck fear] into
        the heart of our city. The secrets lie hidden 
        within a mysterious dataset they have provided-
        each row a piece of the puzzle. Our task, {name},
        is to wield the power of data science to uncover
        the truth behind these heinous acts. 
        """)
    st.divider()
    st.write(f":blue[What shall we do {name}] ? ")
    options = ["""Indeed Mr. Mastermind, let's proceed with analysis .
            The darkness that shrouds these crimes has
            gripped the city with fear.""", "No, The City Can Sort Itself"]
    with st.expander("View Options"):
        proceed = st.radio(":blue[Proceed With Analysis?]", [options[0],options[1]])

        if proceed == options[0]:
            chapter_one(name)        
            experience += 20
            
        elif proceed == options[1]:
            experience -= 1
            
        return experience