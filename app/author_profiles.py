import streamlit as st 
import pandas as pd 
import numpy as np 

def main():

# Use the full page instead of a narrow central column
    bookData = pd.read_csv('app/Data/books.csv')
    author_df = pd.read_csv('app/Data/authors.csv')
    authors = author_df['Name'].unique()
    authorNames = np.insert(authors, 0, "All")
    st.title(f"About the Authors")

    # user inputs 
    authorChoice = st.selectbox('Use the filter to learn more about the authors whose books were used for this project:', authorNames, format_func=lambda x: 'Select an author' if x == '' else x) 
    st.markdown(f'<h2>Featured Authors</h2>', unsafe_allow_html=True)

    if authorChoice =='All': 
        i = 0
        for _ in range(len(authors)-1):
            col = st.beta_columns((1, 1, 1))

            if i < len(authors): 
                col[0].markdown(f'{authors[i]}')
            i+=1
            if i < len(authors): 
                col[1].markdown(f'{authors[i]}')
            i+=1
            if i < len(authors): 
                col[2].markdown(f'{authors[i]}')
                i = i +1
            else:
                break
     

    else:
        filteredBooks = bookData[bookData['Author'] == authorChoice]
        filteredImages = list(filteredBooks['Image'])
        bookCaption = list(filteredBooks['Book'])
        authorFiltered = author_df[author_df['Name'] == authorChoice]
        authors = authorFiltered['Name'].unique()
        authorCaption = list(authorFiltered['Website'])
        st.markdown(list(authorFiltered['Bio'])[0])
        for i in range(len(authorFiltered)):
            st.markdown(f'To learn more about {authors[i]}, visit their [website]({authorCaption[i]})', unsafe_allow_html=True)

        st.markdown(f'<h2>Books by {authorChoice} referenced in this project</h2>', unsafe_allow_html=True)
        idx = 0
        for _ in range(len(filteredImages)): 
            cols = st.beta_columns(4) 
            if idx < len(filteredImages): 
                cols[0].image(filteredImages[idx], width=150, caption = bookCaption[idx] )
                    
            idx+=1
                    
            if idx < len(filteredImages):
                cols[1].image(filteredImages[idx], width=150, caption = bookCaption[idx] )
            idx+=1

            if idx < len(filteredImages):
                cols[2].image(filteredImages[idx], width=150, caption = bookCaption[idx] )
            idx+=1 
            if idx < len(filteredImages): 
                cols[3].image(filteredImages[idx], width=150, caption = bookCaption[idx] )
                idx = idx + 1
            else:
                break

   
