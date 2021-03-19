import streamlit as st 
import pandas as pd 
import numpy as np 

def main():

# Use the full page instead of a narrow central column
    bookData = pd.read_csv('app/Data/books.csv')
    author_df = pd.read_csv('app/Data/authors.csv')
    authors = author_df['Name'].unique()
    authorNames = np.insert(authors, 0, "All")
    authorImages = author_df['Image']
    authorBios = list(author_df['Bio'])
    authorSites = author_df['Website'].unique()
    authorWebsites = np.insert(authorSites, 0, 'All')
    st.title(f"Learn more about the authors")

    # user inputs 
    authorChoice = st.selectbox('Use the filter to learn more about the authors whose books were used for this project:', authorNames, format_func=lambda x: 'Select an author' if x == '' else x) 
    st.markdown(f'<h2>About {authorChoice}</h2>', unsafe_allow_html=True)

    if authorChoice =='All': 
        idx2 = 0  
        for _ in range(len(authorImages)-1):
            with st.beta_container():
                authorCaption = list(author_df['Website'])
                col1, col2 = st.beta_columns((1, 2))
                col1.image(authorImages[idx2], width=200, caption=authors[idx2])
                col2.markdown(authorBios[idx2])
                col2.markdown(f'To learn more visit their [website]({authorCaption[idx2]}).', unsafe_allow_html=True)
                idx2 = idx2+1 
                col2.text("")

    else:
        with st.beta_container():
            col1, col2 = st.beta_columns((1, 1.5))
            authorFiltered = author_df[author_df['Name'] == authorChoice]
            authors = authorFiltered['Name'].unique()
            authorCaption = list(authorFiltered['Website'])
            col1.text(' ')
            col1.image(list(authorFiltered['Image']), use_column_width=True)
            col1.text(' ')
            col2.markdown(list(authorFiltered['Bio'])[0])
            for i in range(len(authorFiltered)):
                col2.markdown(f'To learn more about {authors[i]}, visit their [website]({authorCaption[i]})', unsafe_allow_html=True)


       
            
