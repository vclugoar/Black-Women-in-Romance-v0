import pickle
import streamlit as st 
import itertools 
import pandas as pd 
import gensim 
from random import randrange

# loading the trained model 
pickle_in = open('app/Data/lda.pkl', 'rb')
lda_mod30 = pickle.load(pickle_in)
#bookData = pd.read_csv('books_copy.csv')
bookData = pd.read_csv('app/Data/books.csv')
pickle_in2 = open('app/Data/corpus.pkl', 'rb')
corpus = pickle.load(pickle_in2)

    # define some vars 
bookList = bookData['Book']
bookIndex = bookData['index']
bookAuthor = bookData['Author']
bookLink = bookData['Buy']
bookImage = bookData['Image']
bookDescription = bookData['Description']
index2 = gensim.similarities.MatrixSimilarity(lda_mod30[corpus])


def main(): 
    
    # title 
    st.markdown(f'<h2> Enter a book name to get recommendations based on topic.</h2>', unsafe_allow_html=True)
    st.markdown('Need suggestions? Search through the Book Catalog and Author Spotlight for inspiration!')

    # initialize lists
    corpus_to_compare = []
    names_of_related_books = []
    images_of_related_books = []
    descriptions_of_related_books = []
    authors_of_related_books = []
    links_of_related_books = []

    # user input
    box1, box2 = st.beta_columns(2)
    userSelection = box1.selectbox("Enter a book name:", bookList, index= randrange(0, 392))
    slider = box2.slider("Select level of similarity based on topics", min_value=0.70, max_value=0.99, step=0.01, value=0.85)
    
    descriptionBox = st.checkbox("Show book descriptions", value=False)

    st.markdown(
        f'<h3 style="color: black; ">Books with similar topics to {userSelection}</h3>',
        unsafe_allow_html=True)

    for book in range(len(bookList)):
        if userSelection == bookList[book]:
            corpusA = corpus[bookIndex[book]]
            vec_lda = lda_mod30[corpusA]
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
            links_of_related_books.append(bookLink[book])

    # create columns and add images to each one 
    if descriptionBox == True:
            idx2 = 0  
            for _ in range(len(images_of_related_books)-1):
                with st.beta_container():
                    col1, col2 = st.beta_columns((1, 2.5))
                    col1.image(images_of_related_books[idx2], width=170)
                    col2.markdown(f'<b>{names_of_related_books[idx2]} by {authors_of_related_books[idx2]}:</b> {descriptions_of_related_books[idx2]}', unsafe_allow_html=True)  
                    col2.write(f'Buy the book [here]({links_of_related_books[idx2]}).') 
                    #col2.markdown(f'{descriptions_of_related_books[idx2]}')
                    #for i in range(len(descriptions_of_related_books)):
                    #    col2.markdown(f'<b>{names_of_related_books[i]} by {authors_of_related_books[i]}:</b> {descriptions_of_related_books[i]}', unsafe_allow_html=True)   
                    idx2 = idx2+1 
                    col2.text("") 
    else: 
        idx = 0
        for _ in range(len(images_of_related_books)-1): 
            cols = st.beta_columns(3) 
            
            if idx < len(images_of_related_books)-1:
                cols[0].image(images_of_related_books[idx], width=175, caption=f'{names_of_related_books[idx]} by {authors_of_related_books[idx]}')
            idx+=1

            if idx < len(images_of_related_books)-1:
                cols[1].image(images_of_related_books[idx], width=175, caption=f'{names_of_related_books[idx]} by {authors_of_related_books[idx]}')
            idx+=1 
            if idx < len(images_of_related_books)-1: 
                cols[2].image(images_of_related_books[idx], width=175, caption=f'{names_of_related_books[idx]} by {authors_of_related_books[idx]}')
                idx = idx + 1
            else:
                break
         

        
            # st.markdown('<h2>Book Descriptions</h2>', unsafe_allow_html=True)
            # col1, col2 = st.beta_columns((10, 1))

 
            # #col1.image(images_of_related_books, width=200)
            # for i in range(len(descriptions_of_related_books)):
            #     col1.markdown(f'<b>{names_of_related_books[i]} by {authors_of_related_books[i]}:</b> {descriptions_of_related_books[i]}', unsafe_allow_html=True)   

