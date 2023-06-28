import streamlit as st
import time

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
            points_attained = 2
            return points_attained