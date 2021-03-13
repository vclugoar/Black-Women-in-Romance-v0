import pickle
import streamlit as st 
import itertools 
import pandas as pd 
from gensim import similarities

# loading the trained model 
pickle_in = open('lda.pkl', 'rb')
lda_mod25 = pickle.load(pickle_in)
bookData = pd.read_csv('books.csv')
pickle_in2 = open('corpus.pkl', 'rb')
corpus = pickle.load(pickle_in2)

# define some vars 
bookList = bookData['Book']
bookIndex = bookData['index']
bookAuthor = bookData['Author']
bookImage = bookData['Image']
bookDescription = bookData['Description']
index2 = similarities.MatrixSimilarity(lda_mod25[corpus])

def app(userSelection): 
    corpus_to_compare = []
    names_of_related_books = []
    images_of_related_books = []
    descriptions_of_related_books = []
    authors_of_related_books = []

    slider = st.slider("Select level of similarity based on topics", min_value=0.0, max_value=1.0, step=0.01, value=0.97)
    
    for book in range(1, 339):
        if userSelection == bookList[book]:
            corpusA = corpus[bookIndex[book]]
            vec_lda = lda_mod25[corpusA]
            corpus_to_compare.append(vec_lda)

    sim = index2[vec_lda]
    sims = sorted(enumerate(sim), key=lambda item: -item[1])
    # let users select how similar books 
    DoublelistOfRelatedBooks = [list(group) for val, group in itertools.groupby(sims, lambda x: x[1] >= slider) if val]
    listOfRelatedBooks = DoublelistOfRelatedBooks[0]

    # split tuples into two lists with book name and similarity score 
    book_name, score = map(list, zip(*listOfRelatedBooks))

    # iterate to get the name of the books and not the book index 
    for book in book_name:
        if (bookIndex[book]== book_name).any():
            names_of_related_books.append(bookList[book])
            images_of_related_books.append(bookImage[book]) 
            descriptions_of_related_books.append(bookDescription[book])
            authors_of_related_books.append(bookAuthor[book])

    # create columns and add images to each one 
    idx = 0
    for _ in range(len(images_of_related_books)-1): 
        cols = st.beta_columns(3) 
        
        if idx < len(images_of_related_books):
            cols[0].image(images_of_related_books[idx], width=175, caption=names_of_related_books[idx])
        idx+=1

        if idx < len(images_of_related_books):
           cols[1].image(images_of_related_books[idx], width=175, caption=names_of_related_books[idx])
        idx+=1 
        if idx < len(images_of_related_books): 
            cols[2].image(images_of_related_books[idx], width=175, caption=names_of_related_books[idx])
            idx = idx + 1
        else:
            break
         
    with st.beta_container():
        st.markdown('<h2>Book Descriptions</h2>', unsafe_allow_html=True)
        col1, col2 = st.beta_columns((10, 1))

 
        #col1.image(images_of_related_books, width=200)
        for i in range(len(descriptions_of_related_books)):
            col1.markdown(f'<b>{names_of_related_books[i]} by {authors_of_related_books[i]}:</b> {descriptions_of_related_books[i]}', unsafe_allow_html=True)   

