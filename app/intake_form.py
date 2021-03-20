import streamlit as st 
import pandas as pd 
import numpy as np 

def main():

    # brief about 
    with st.beta_container():
        st.markdown("""
        The Black Women in Romance project started as a capstone for the MS in Data Analysis and Visualization program at the CUNY graduate Center for the Spring of 2021.
        
        The lists of authors and books are in no way exhaustive, and I will expand the catalog to include more books when funds allow (buying books is expensive!).

        If you have a book or author in mind not currently part of the project, please enter the author's names or book titles below to include in future iterations of the project.

    """)
        #st.image('https://i.ibb.co/NmhK4yY/Hello-This-tool-started-as-a-capstone-project-for-the-MS-in-Data-Analysis-and-Visualization-program.png', use_column_width=True)
    
    # form 
    with st.beta_container():
        st.markdown('<h2> Would you like to add a book or author?</h2>', unsafe_allow_html=True)
        st.markdown('<h4>Book Name(s)</h4>', unsafe_allow_html=True)
        newBookName = st.text_area("Please enter the book name(s), separated by commas")
        st.markdown('<h4>Author Name(s)</h4>', unsafe_allow_html=True)
        newBookAuthor = st.text_area("Enter the author name(s), separated by commas")

        st.markdown('<h2> Any questions, feedback or recommendations? </h2>', unsafe_allow_html=True)
        newFeedback = st.text_area("Enter questions, feedback or recommendations")

        st.markdown('<h2> Would you like to receive email updates about this or similar projects?</h2>', unsafe_allow_html=True)
        st.markdown('<h4> If so, enter your contact information below</h4>', unsafe_allow_html=True)
        emailName = st.text_input('Enter name')
        emailAddress = st.text_input('Enter a valid email address')

        # submit button 
        clickSubmit = st.button('Submit')

        if clickSubmit == True:
            st.markdown('<h3>Thank you for your feedback!</h3>', unsafe_allow_html=True)
            # save into dictionary and then dataframe 
            d = {'Book Name(s)': [newBookName], 
                'Book Author(s)': [newBookAuthor],
                'Feedback': [newFeedback],
                'Name': [emailName],
                'Email': [emailAddress]}
            df = pd.DataFrame(data=d)
            st.markdown('Submitted responses:')
            st.write(df)
        
        else:
            st.markdown("Click submit to save form responses.")

#app()

