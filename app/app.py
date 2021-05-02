import book_recommendation
import book_choices
import author_profiles
import about 
import intake_form
#import aboutme
import streamlit as st 
import pandas as pd 

st.set_page_config(page_title='Black Women in Romance', layout='centered')

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


# get the pages on nav
PAGES = { 
    "How to Use": about,
    "Book Catalog": book_choices,
    "Book Recommendations": book_recommendation,  
    "Author Spotlight": author_profiles,
    "Add Books or Authors": intake_form
   # "About": aboutme
}

# get data
bookData = pd.read_csv('app/Data/books.csv')
bookList = bookData['Book'].unique()

# user interaction 
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]

# navigation and user interaction 
if selection == 'How to Use':
    st.image('https://i.ibb.co/cFfvYJs/1.png', use_column_width=True)
    page.main()
elif selection == 'Book Catalog':
    st.image('https://i.ibb.co/527LgRd/2.png', use_column_width=True)
    page.main()
elif selection == 'Book Recommendations':
    st.image('https://i.ibb.co/G55FZs0/3.png', use_column_width=True)
    page.main()
elif selection == 'Author Spotlight':
    st.image('https://i.ibb.co/5618csr/4.png', use_column_width=True)
    page.main()
elif selection == 'Add Books or Authors':
    st.image('https://i.ibb.co/qdDzWC0/Page-banners-2.png')
    page.main()
elif selection == 'About':
    page.main()

st.sidebar.markdown('<h5>Created by Vianny Lugo-Aracena</h5>', unsafe_allow_html=True)
