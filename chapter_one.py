import streamlit as st
import time
from multiverse.verse_one.verse_one import verse_one_alternatives

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
                          Date      Location    Crime_Type      Suspects  Witnesses
                       2023-01-15   Baker St.   Robbery            1         3
                       2023-01-18   Park Rd.    Assault            2         1
                       2023-01-21   Elm St.     Burglary           3         2
                       2023-01-24   Maple Ave.  Robbery            2         4
                       2023-01-25   Baker St.   Assault            1         2

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
                    |         | Suspects  | Witnesses
                        count  100.00000    100.00000
                        mean     2.17000    2.29000
                        std      0.92707    1.15675
                        min      1.00000    1.00000
                        25%      1.00000    1.00000
                        50%      2.00000    2.00000
                        75%      3.00000    3.00000
                        max      4.00000    5.00000


                """, line_numbers=True
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
            
            
            points_attained = 2
            return points_attained