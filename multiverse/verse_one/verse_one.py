
from multiverse.verse_one.verse_one_data import describe_data
from multiverse.verse_one.verse_one_data import dataset_frame


import streamlit as st

def verse_one_alternatives(name , alternatives = describe_data):
    choice = st.radio("Choose response", alternatives)
    if choice == describe_data[0]:
        st.caption(":red[**The Mastermind**]")

        st.info(f"""
                By all means, {name}. Unleash the power of statistics, and let us grasp the magnitude of our investigation.
            """)
        st.code(f"""
        # Unveil the secrets with summary statistics
        {dataset_frame.describe()}
        """, line_numbers=True)
    elif choice == describe_data[1]:
        st.caption(":red[**The Mastermind**]")

        st.info(f"""
            You're right, {name}. 
            This ledger of crime provides a window into the 
            underworld's activities. The dates and locations are like puzzle pieces, 
            waiting to be assembled to reveal the bigger picture. With every clue we decipher, 
            we inch closer to shedding light on the darkness that plagues our beloved city.                
            Together, we shall unlock the truth.
        """)
        st.code(f"""
        # Unveil the secrets with summary statistics
        { dataset_frame.describe() }
        """, line_numbers=True)


    
 


                