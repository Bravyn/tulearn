import streamlit as st
import time
from multiverse.verse_one.verse_one import verse_one_alternatives
from multiverse.verse_one.verse_one_data import dataset_frame


def chapter_one(name):
    
    st.caption("**:red[The Mastermind]:**")
    st.info("We shall unravel everything. Let\
             us summon the enigmatic **Pandas**\
              library to our aid and delve into\
             the depths of this treacherous dataset: ")
    code = """
    import pandas as pd

    #unveil the dataset
    crime_data = pd.read_csv('crime_data.csv')
    """
    st.code(code, line_numbers=True)
    options = ["The dataset, like a hidden vault,\
               has been unlocked, Mr. Mastermind. It\
               lies before our very eyes. Waiting to\
               to divulge it's secrets. Shall we take our\
               first steps and examine it's structure?", 
               "I have another idea"]
    
    choices = st.radio(":red[Respond to the Mastermind:]",options )
    if choices == options[0]:
        with st.container():
            st.caption(f":blue[**{name}**]")
            st.info(choices)
            st.caption(":red[**The Mastermind**]")
            st.info(f"Indeed, {name}. Cast your gaze\
                    upon the first few rows of the \
                    dataset. Let us glimpse into the\
                    the shadows that haunt our city.")
        code = """
                #Illuminate the shadows with the first few rows
                crime_data.head()
            """
        st.code(code, line_numbers= True)
        with st.container():
            st.caption(f":blue[**{name}**]")
            st.info("Behold Mastermind! The shadows begin to take shape.")
            
            code2 = """
                       date    location crime_type  suspects  witnesses
                   2022-10-19     Home    Robbery         4          0
                   2022-10-19     Work    Assault         0          1
                   2022-10-19   Street     Murder         2          3
                   2022-10-19    Store      Fraud         4          3
                   2022-10-19    Store    Assault         4          0

            """
            st.code(code2)

            st.caption(":red[**The Mastermind**]")
            st.info(f"Fascinating, {name}! Each row is a glimpse into the darkness that engulfs our city. \
                    Dates, locations, crime types—they all hold the key to our investigation.")
            st.caption(f":blue[**{name}**]")
            verse_one_alternatives(name)
            st.caption(f":blue[**{name}**]")
            st.info("The secrets, Mastermind—they begin to reveal themselves.")
            st.code(
               """
              |        |  suspects   |  witnesses
                count    200.000000    200.000000
                mean     2.470000      2.370000
                std      1.680243      1.632921
                min      0.000000      0.000000
                25%      1.000000      1.000000
                50%      3.000000      2.000000
                75%      4.000000      4.000000
                max      5.000000      5.000000
                """, 
line_numbers=True
            )
            st.caption(":red[**The Mastermind**]")
            st.info(f"""
               The secrets have begun to whisper, {name}. 
               On average, each crime hides approximately two suspects and two witnesses within its murky depths.
               But remember, Watson, the range of suspects and witnesses may hold the key to unraveling these mysteries.
            """)
            st.caption(f":blue[**{name}**]")
            st.info("The secrets unfold before us, Mastermind. How shall we proceed further on this treacherous path?")
            st.caption(":red[**The Mastermind**]")
            st.info("""
               We shall illuminate the shadows, Watson. 
               Visualization shall be our torch, 
               revealing patterns hidden from mortal eyes.
               Arm yourself with the tools of Matplotlib.

            """)
            st.code("""
                import matplotlib.pyplot as plt

                # Unveil the patterns with a plot of crime type distribution
                crime_data['Crime_Type'].value_counts().plot(kind='bar')
                plt.xlabel('Crime Type')
                plt.ylabel('Frequency')
                plt.title('Distribution of Crime Types')
                plt.show()


            """)  




            st.caption(":red[**The Mastermind**]")
            st.caption("Do you wish to Continue playing?")
            st.caption("Email me at ianbravyns@gmail.com your answer")
            
            
            points_attained = 4
            return points_attained