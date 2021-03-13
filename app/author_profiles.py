import streamlit as st 
import itertools 
import pandas as pd 
import numpy as np 

#st.beta_set_page_config(layout="wide")

def app():

# Use the full page instead of a narrow central column
    bookData = pd.read_csv('books.csv')
    author_df = pd.read_csv('authors.csv')
    authors = author_df['Name']
    st.title(f"Author Spotlight")
    authorChoice = st.selectbox('Use the filter to learn more about the authors whose books were used for this project:', authors, format_func=lambda x: 'Select an author' if x == '' else x) 

    st.markdown(f'<h2>About {authorChoice}</h2>', unsafe_allow_html=True)
    with st.beta_container():
        col1, col2 = st.beta_columns((1, 1.5))

        authorFiltered = author_df[author_df['Name'] == authorChoice]
        authorCaption = list(authorFiltered['Website'])
        col1.text(' ')
        col1.text(' ')
        col1.image(list(authorFiltered['Image']), use_column_width=True, caption = authorCaption)
        col1.text(' ')
        col1.text(' ')
        col2.write(list(authorFiltered['Bio']))

    st.title(f"Books by {authorChoice}")
    st.markdown(f"<h2>Books written by {authorChoice} that were used for this project.</h2>", unsafe_allow_html=True)
    
    with st.beta_container():
        colh, colh2 = st.beta_columns((6, 1))

        authorFiltered = author_df[author_df['Name'] == authorChoice]
        bookFiltered = bookData[(bookData['Author'] == authorChoice)]

        filteredImages = list(bookFiltered['Image'])
        filteredTitles = list(bookFiltered['Book'])
        caption = list(filteredTitles)

        idx = 0 
        for _ in range(len(filteredImages)-1): 
            cols = st.beta_columns(4) 
            
            if idx < len(filteredImages): 
                cols[0].image(filteredImages[idx], width=150, caption=caption[idx])
            idx+=1
            
            if idx < len(filteredImages):
                cols[1].image(filteredImages[idx], width=150, caption=caption[idx])
            idx+=1

            if idx < len(filteredImages):
                cols[2].image(filteredImages[idx], width=150, caption=caption[idx])
            idx+=1 
            if idx < len(filteredImages): 
                cols[3].image(filteredImages[idx], width=150, caption=caption[idx])
                idx = idx + 1
            else:
                break
        #colh.markdown(list(authorFiltered['Bio']))

   # c1, c2, c3, c4 = st.beta_columns((2, 1, 1, 1))

#authors()
