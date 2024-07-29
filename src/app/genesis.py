import streamlit as st
from chapter_one import chapter_one    
from intro_card import cards


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
            name = name.capitalize()
            st.caption("The Mastermind:")

            cards([f"""
                    Very well, Mr. {name}. If you believe the city is capable of sorting itself, we shall respect your decision. However, let us not forget our duty as detectives and the impact our actions can have on the lives of the innocent.
                    While the city grapples with fear, chaos, and uncertainty, our skills and expertise could provide a guiding light. Our analytical minds and unwavering determination might be the catalyst the city needs to restore order and bring the perpetrators to justice.
                    Should you change your mind or feel compelled to take action, I shall be here, ready to assist you in your pursuit of the truth. The choice remains yours, Mr. {name}, and I stand ready to support you, whether it be through analysis or alternative means.
                    Remember, the city's fate lies in your hands, and your decisions will shape its destiny.
            """])
            experience -= 1
            
        return experience