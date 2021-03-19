import streamlit as st 
import pandas as pd 
import numpy as np 

def main(): 
    #bookData = pd.read_csv('books_copy.csv')
    bookData = pd.read_csv('app/Data/books.csv')
    bookAuthor = bookData['Author'].unique()
    authors = np.insert(bookAuthor, 0, 'All')
    bookTopic = bookData['max_col'].unique()
    topics = np.insert(bookTopic, 0, 80)
    year_a = bookData['Year'].unique()
    years = np.insert(year_a, 0, 0)
    years.sort()
    

    #st.markdown(f'<h2>Use filters by topic and author or scroll down to explore the books used to build the LDA-based recommendation system</h3>', unsafe_allow_html=True)
    st.subheader('Use filters by topic and author or scroll down to explore the books used to build the LDA-based recommendation system')
    
    box1, box2, box3 = st.beta_columns(3)
    authorChoice = box1.selectbox('Filter by author:', authors, format_func=lambda x: 'Filter by author' if x == '' else x, key='All')
    topicChoice = box2.selectbox('Filter by topic:', topics, format_func=lambda x: 'Filter by topic' if x == '' else x)
    yearChoice = box3.selectbox('Filter by year:', years, format_func=lambda x: 'Filter by topic' if x == '' else x)
    descriptionChoiceC = st.checkbox('Show book descriptions', value=False)

    st.markdown(f'Books written by {authorChoice}, with the topic {topicChoice}',
        unsafe_allow_html=True)

    if (authorChoice == 'All') & (topicChoice == 80) & (yearChoice == 0):
       st.image('https://i.ibb.co/X3Dpz54/Use-the-filters-above-to-see-books-2.png', use_column_width=True)
    else: 
        bookFiltered = bookData[(bookData['Author'] == authorChoice) | (bookData['max_col'] == topicChoice) | (bookData['Year'] == yearChoice)]
        filteredImages = list(bookFiltered['Image'])
        filteredTitles = list(bookFiltered['Book'])
        filteredDescription = list(bookFiltered['Description'])
        filteredLink = list(bookFiltered['Buy'])
        filteredAuthors = list(bookFiltered['Author'])
        caption = list(filteredTitles)

        if descriptionChoiceC == True: 
            idx2 = 0  
            for _ in range(len(filteredImages)):
                with st.beta_container():
                    col1, col2 = st.beta_columns((1, 2))
                    col1.image(filteredImages[idx2], width=200)
                    col2.markdown(f'<b>{filteredTitles[idx2]} by {filteredAuthors[idx2]}:</b> {filteredDescription[idx2]}', unsafe_allow_html=True)
                    #col2.markdown(f'')
                    col2.write(f'Buy the book [here]({filteredLink[idx2]}).')
                    idx2 = idx2+1 
                    col2.text("")
        else: 
            idx = 0 
            for _ in range(len(filteredImages)): 
                cols = st.beta_columns(4) 
                
                if idx < len(filteredImages): 
                    cols[0].image(filteredImages[idx], width=150, caption=f'{caption[idx]} by {filteredAuthors[idx]}')
                   
                idx+=1
                
                if idx < len(filteredImages):
                    cols[1].image(filteredImages[idx], width=150, caption=f'{caption[idx]} by {filteredAuthors[idx]}')
                idx+=1

                if idx < len(filteredImages):
                    cols[2].image(filteredImages[idx], width=150, caption=f'{caption[idx]} by {filteredAuthors[idx]}')
                idx+=1 
                if idx < len(filteredImages): 
                    cols[3].image(filteredImages[idx], width=150, caption=f'{caption[idx]} by {filteredAuthors[idx]}')
                    idx = idx + 1
                else:
                    break
                

