import streamlit as st 
import itertools 
import pandas as pd 
import numpy as np 

def app():

    bookData = pd.read_csv('app/books.csv')
  #  bookDescription = list(bookData['Description'])
    bookImage = list(bookData['Image'])
    books = bookData['Book'] 
    bookChoice = st.selectbox('Select a book to learn more', books, format_func=lambda x: 'Select a book' if x == '' else x) 

    filteredBook = bookData
    #filteredBook = bookData[bookData['Book'] ==bookChoice]
    filteredImage = list(filteredBook['Image'])
    filteredDescription = list(filteredBook['Description'])

    idx = 0  
    for _ in range(len(filteredBook)):
        with st.beta_container():
            col1, col2 = st.beta_columns((1, 1.5))
          # for book in 
            col1.image(filteredImage[idx], width=250)
           # idx+=1
            col2.markdown(f'{filteredDescription[idx]}')
            idx = idx+1 
            col2.text("")


# old code for showing all images in the catalog 
 # if descriptionChoiceC == True: 
        #     idx2 = 0  
        #     for _ in range(len(all_images)):
        #         with st.beta_container():
        #             col1, col2 = st.beta_columns((1, 1.5))
        #             col1.image(all_images[idx2], width=250)
        #             col2.markdown(f'{bookDescription[idx2]}')
        #             idx2 = idx2+1 
        #             col2.text("")
        # else:
        #     idx = 0 
        #     for _ in range(len(all_images)-1): 
        #         cols = st.beta_columns(4) 
        #         cols[0].image(all_images[idx], width=150, caption=bookList[idx])
        #         idx+=1
        #         cols[1].image(all_images[idx], width=150, caption=bookList[idx])
        #         idx+=1
        #         cols[2].image(all_images[idx], width=150, caption=bookList[idx])
        #         idx+=1 
        #         if idx < len(all_images): 
        #             cols[3].image(all_images[idx], width=150, caption=bookList[idx])
        #             idx = idx + 1
        #         else:
        #             break


app()
