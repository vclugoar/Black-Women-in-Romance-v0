import pickle
import streamlit as st 
import itertools 
import pandas as pd 
from gensim import similarities
from PIL import Image
import requests
from io import BytesIO

#from paginator import paginator


bookData = pd.read_csv('books.csv')
bookList = bookData['Book']


def app(): 
    
    bookAuthor = bookData['Author'].unique()
    bookTopic = bookData['max_col'].unique()

    authorChoice = st.sidebar.selectbox('Filter by author:', bookAuthor, format_func=lambda x: 'Filter by author' if x == '' else x)
    #topicChoice = st.sidebar.selectbox('Filter by topic', bookTopic  )

    st.markdown(
        f'<h2 style="color: black;">Books written by {authorChoice}</h2>',
        unsafe_allow_html=True)


    bookFiltered = (bookData[bookData['Author'] == authorChoice]) 
    filteredImages = list(bookFiltered['Image'])
    filteredTitles = list(bookFiltered['Book'])
    # resizedImages = []

    # for image in filteredImages:
    #     r = requests.get(image)
    #     img = Image.open(BytesIO(r.content))
    #     resizedImg = img.resize((225, 325), Image.ANTIALIAS)
    #     resizedImages.append(resizedImg)


    #images = list(filteredImages)
    caption = list(filteredTitles)

    # with st.beta_container():
    #     for col in st.beta_columns(4):
   
    #         col.image(filteredImages, use_column_width=150)

    st.image(filteredImages, width=150, caption=caption)

