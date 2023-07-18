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
    if choices == options[1]:
        
        suggestions = ["Investigate the data source", 
                       "Conduct exploratory data analysis (EDA)",
                       "Seek external assistance",
                       "Explore alternative data sources",
                       "Gather domain-specific knowledge"

                       ]
        
        choose_sugg = st.radio(":blue[**SELECT RELATED IDEA: :point_down:**] ", suggestions)
        
        if choose_sugg == suggestions[0]:
            st.caption(":red[**The Mastermind**]")

            st.info(
               
                f"""
                    Ah, my dear {name}, it appears we shall embark on a quest to uncover the secrets behind the data source! Just as I have deduced many a mystery from the tiniest of details, we shall delve into the origin and collection process of this dataset with our keen detective skills.

                    Let us don our metaphorical deerstalker hats and start our investigation. First, we shall employ our powers of research, scouring the depths of the digital realm for any information on the data provider. We must uncover their motives, reputation, and any clues they might have left behind.

                    Next, we shall turn our attention to the accompanying documentation, my dear {name}. It is within those hidden pages that we may find the key to understanding the dataset's purpose and its potential secrets. Every word, every sentence may hold the clue that unlocks the door to enlightenment.

                    But, my dear {name}, let us not forget the power of human interaction. We must seek out those who may have knowledge of the dataset's collection process. Through interviews and conversations, we shall extract valuable insights, like gems hidden in plain sight.

                    And as we progress, my dear {name}, we shall weave together the threads of information, forming a tapestry of understanding. We shall identify any inconsistencies or peculiarities, for no detail shall escape our watchful eyes.

                    With each step we take, my dear {name}, we bring ourselves closer to the truth. Let us proceed with determination and tenacity, for in the investigation of the data source lies the path to unraveling the secrets that await us.
                """
            )
        elif choose_sugg == suggestions[1]:
            st.caption(":red[**The Mastermind**]")

            st.info(
               
                f"""
                    Excellent choice, my astute {name}. Conducting exploratory data analysis (EDA) is a crucial step in our investigation, as it allows us to unravel the hidden patterns and insights within the dataset. Together, we shall embark on this journey of discovery.

                    First, let us gather the dataset before us, carefully examining its contents. We shall calculate basic statistics, such as means, medians, and standard deviations, to gain an initial understanding of the data's central tendencies and variabilities.

                    Next, we shall venture deeper, my inquisitive {name}. Through data visualization techniques, we can uncover visual patterns and anomalies that may have eluded our initial observations. Scatter plots, histograms, and box plots shall serve as our magnifying glass, revealing valuable clues about relationships, distributions, and potential outliers.

                    But our investigation does not stop there, my tenacious {name}. We must meticulously inspect the data for missing values, inconsistencies, or errors that might hinder our progress. By cleaning and preparing the data, we ensure the reliability and integrity of our analysis.

                    Additionally, let us explore the correlations between variables, seeking out dependencies and interconnections that might hold the key to the secrets we seek. By analyzing covariance matrices or employing techniques such as correlation heatmaps, we can identify potential relationships that might guide us closer to the truth.

                    As we progress through this phase of EDA, my diligent {name}, we shall not only uncover the mysteries concealed within the dataset but also generate initial hypotheses that will guide us towards our ultimate goal. These hypotheses shall serve as guiding stars in our pursuit of truth and understanding.

                    So, my dear {name}, let us dive into the depths of the data, armed with our statistical tools and visualization techniques. Together, we shall unravel the intricacies and unveil the hidden narratives that lie within, bringing us one step closer to solving the grand puzzle before us.
                """
            )
        elif choose_sugg == suggestions[2]:
            st.caption(":red[**The Mastermind**]")

            st.info(
               
                f"""
                    Ah, my dear {name}, your intuition leads us to seek external assistance in our quest to uncover the secrets hidden within the dataset. Just as a great detective knows the value of collaboration, we shall reach out to experts and fellow detectives to aid us in this intricate investigation.

                    Together, we shall form a formidable team, pooling our collective knowledge and expertise. Our first step is to identify these knowledgeable individuals who can lend their unique perspectives to our endeavor. We shall seek out data scientists, statisticians, and other professionals well-versed in the realm of data analysis.

                    With our team assembled, we shall convene in our detective headquarters, a space buzzing with intellectual energy and investigative fervor. In this collaborative atmosphere, we shall share our initial findings, pose questions, and brainstorm innovative approaches to unravel the dataset's secrets.

                    Each team member shall bring their own set of skills and experiences to the table. Through lively discussions, debates, and insights, we shall refine our hypotheses and develop new lines of inquiry. We may encounter challenges and roadblocks along the way, but with determination and the collective wisdom of our team, we shall overcome them.

                    Furthermore, our external assistance need not be limited to our immediate team. We may also tap into the vast network of resources and knowledge available to us. We can reach out to researchers, industry experts, or even consult with unconventional sources to gain new perspectives and fresh insights into the mysteries we face.

                    Through collaboration and a diversity of perspectives, my dear {name}, we shall navigate the twists and turns of this investigation. Together, we shall harness the power of collective intelligence, propelling us closer to the truth and unearthing the secrets hidden within the dataset.

                    So, let us embrace the spirit of collaboration and set forth on this journey, knowing that with the combined efforts of our team, we are well-equipped to conquer the challenges that lie ahead. Onward, dear {name}, as we embark on this collaborative endeavor to crack the code and unlock the hidden truths within the dataset!
                """
            )
        elif choose_sugg == suggestions[3]:
            st.caption(":red[**The Mastermind**]")
            st.info(f"""
                    Ah, an excellent choice, my inquisitive {name}! If the dataset at hand doesn't reveal all the answers we seek, it's time to venture into the realm of alternative data sources. Just as a detective pursues different leads, we shall explore new avenues in our quest for knowledge.

                    First, we shall broaden our search beyond the confines of the current dataset. We'll dig deep into the vast digital landscape, scouring databases, repositories, and any other potential treasure troves that might hold relevant information. A meticulous examination of related datasets may provide the missing puzzle pieces we need to solve the mystery at hand.

                    But let us not limit ourselves to traditional sources alone, {name}. We must think outside the box and consider unconventional sources that might harbor unexpected insights. It could be social media platforms, open data initiatives, or even specialized forums where domain experts gather to exchange knowledge. The digital world is a vast and varied landscape, and we must navigate it with an open mind.

                    As we gather data from these alternative sources, we shall weave together different threads of information, drawing connections and forming a more comprehensive picture. Through careful analysis and cross-referencing, we may uncover hidden patterns, correlations, or unique perspectives that were previously concealed.

                    Be prepared, my intrepid {name}, for this path may be strewn with challenges and the need for discernment. We must exercise caution and critical thinking to ensure the reliability and validity of the alternative data sources we encounter. But fear not, for it is through such rigorous investigation that we pave the way to a deeper understanding of the enigma before us.

                    So, let us embark on this journey, {name}, exploring alternative data sources with the determination of a detective in pursuit of the truth. Together, we shall uncover the hidden secrets that lie beyond the confines of the initial dataset, and unravel a mystery that will leave even the most cunning minds astounded.
                    
                """)
        elif choose_sugg == suggestions[4]:
            st.caption(":red[**The Mastermind**]")
            st.info(f"""
                    Ah, a wise choice, my dear {name}! To gather domain-specific knowledge is to arm ourselves with the necessary insights to unravel the mysteries hidden within the dataset. Let us embark on a journey of learning and understanding.

                    We shall delve deep into the subject matter of the dataset, immersing ourselves in its intricacies. Research shall be our ally, guiding us through the vast expanse of knowledge related to the domain. We shall consult reputable sources, academic papers, industry reports, and the wisdom of experts.

                    Every piece of information we acquire will be like a puzzle piece, fitting into the grand picture we seek to reveal. We shall become familiar with the terminology, concepts, and underlying principles of the domain, allowing us to approach the dataset with a discerning eye.

                    Our quest for domain-specific knowledge shall not be limited to conventional sources alone. We shall explore unconventional avenues, seeking unconventional wisdom. Perhaps we shall uncover insights from unconventional experts, such as practitioners, enthusiasts, or even those who possess unique perspectives on the subject matter.

                    As we gather this wealth of knowledge, my dear {name}, we shall grow in understanding and intuition. We shall be equipped to ask the right questions, spot meaningful patterns, and formulate hypotheses that transcend the mere data itself.

                    Remember, my dear {name}, that knowledge is power. The deeper our understanding of the domain, the sharper our investigative skills become. Let us embrace this opportunity to become true experts in the field, for it is through domain-specific knowledge that we shall unlock the most profound secrets hidden within the dataset.

                    Onward we go, my dear {name}, into the depths of knowledge, as true detectives of the data science realm.
                """)




        return 4