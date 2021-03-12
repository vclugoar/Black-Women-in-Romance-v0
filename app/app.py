import book_recommendation
import book_choices
import author_profiles
import streamlit as st 
from annotated_text import annotated_text, annotation


PAGES = {   
    "Book Recommendation": book_recommendation,
    "Book Choices": book_choices,
    "Author Profiles": author_profiles
    
}
# https://i.ibb.co/kSpRrsL/Copy-of-Storytelling-with-data.png
#https://i.ibb.co/fNL0YN0/Copy-of-Storytelling-with-data.jpg'
#https://i.ibb.co/7pzSWkq/Untitled-design-High-Quality.jpg
st.image('https://i.ibb.co/PzJPXfW/Copy-of-Copy-of-Storytelling-with-data.png', use_column_width=True)
    #'g', use_column_width=True)
#
#''
# st.markdown(
#         f'<h1 style="color: FireBrick;">Black Women in Romance Genre</h1>',
#         unsafe_allow_html=True
# )

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]

if selection == 'Book Recommendation':
    st.subheader(f'LDA-Based Book Recommendation for Romance Novels Written by Black Women')
    st.text('Need suggestions? Search through Book Choices and Author Profiles for inspiration!')
    userSelection = st.text_input("Enter a book name:", 'Make a Scene')

    st.markdown(
        f'<h3 style="color: black; ">Books with similar topics to {userSelection}</h3>',
        unsafe_allow_html=True)
    page.app(userSelection)
#elif (selection == 'Book Choices' | selection == 'Author Profiles'):
else:
    page.app()
