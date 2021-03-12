import pickle
import streamlit as st 
import itertools 
import pandas as pd 
from gensim import similarities
from PIL import Image
import requests
from io import BytesIO
import numpy as np 

def app(): 
    bookData = pd.read_csv('books.csv')
    bookList = bookData['Book']
    bookAuthor = bookData['Author'].unique()
    authors = np.insert(bookAuthor, 0, 'All')
    bookTopic = bookData['max_col'].unique()
    topics = np.insert(bookTopic, 0, 80)


    authorChoice = st.sidebar.selectbox('Filter by author:', authors, format_func=lambda x: 'Filter by author' if x == '' else x)
    topicChoice = st.sidebar.selectbox('Filter by topic:', topics, format_func=lambda x: 'Filter by topic' if x == '' else x)

    st.markdown(
        f'<h3 style="color: black;">Books written by {authorChoice}, with the topic {topicChoice}</h3>',
        unsafe_allow_html=True)

    all_images = list(bookData['Image'])
    if (authorChoice == 'All') & (topicChoice == 80):
        idx = 0 
        for _ in range(len(all_images)-1): 
            cols = st.beta_columns(4) 
            cols[0].image(all_images[idx], width=150, caption=bookList[idx])
            idx+=1
            cols[1].image(all_images[idx], width=150, caption=bookList[idx])
            idx+=1
            cols[2].image(all_images[idx], width=150, caption=bookList[idx])
            idx+=1 
            if idx < len(all_images): 
                cols[3].image(all_images[idx], width=150, caption=bookList[idx])
                idx = idx + 1
            else:
                break
    else: 
        bookFiltered = bookData[(bookData['Author'] == authorChoice) | (bookData['max_col'] == topicChoice)]
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
                
       