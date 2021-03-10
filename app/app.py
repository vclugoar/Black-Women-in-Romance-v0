import book_recommendation
import book_choices
import streamlit as st 
from annotated_text import annotated_text, annotation


PAGES = {
    "Book Choices": book_choices,
    "Book Recommendation": book_recommendation
}

st.markdown(
        f'<h1 style="color: green;">Black Women in Romance Genre</h1>',
        unsafe_allow_html=True)


st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]

if selection == 'Book Recommendation':
    
    userSelection = st.text_input("Enter a book name, reference Book Choices page for inspiration", 'Make a Scene')
    st.markdown(
        f'<h2 style="color: black; ">Find books with similar topics to {userSelection}</h2>',
        unsafe_allow_html=True)
   # st.title("Here's your list:")
    page.app(userSelection)
elif selection == 'Book Choices':
    page.app()
