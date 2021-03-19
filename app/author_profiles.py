import streamlit as st 
import pandas as pd 
import numpy as np 

def main():

# Use the full page instead of a narrow central column
   # bookData = pd.read_csv('app/Data/books.csv')
    author_df = pd.read_csv('app/Data/authors.csv')
    authors = author_df['Name'].unique()
    authorNames = np.insert(authors, 0, "All")
    authorImages = author_df['Image']
    authorBios = list(author_df['Bio'])
    authorSites = author_df['Website'].unique()
    authorWebsites = np.insert(authorSites, 0, 'All')
    st.title(f"Learn more about the authors")

    # user inputs 
   # showBooks = st.checkbox('Show author books referenced')
    authorChoice = st.selectbox('Use the filter to learn more about the authors whose books were used for this project:', authorNames, format_func=lambda x: 'Select an author' if x == '' else x) 
    st.markdown(f'<h2>About {authorChoice}</h2>', unsafe_allow_html=True)

    if authorChoice =='All': 
        idx2 = 0
        for _ in range(len(authorImages)-1):
                authorCaption = list(author_df['Website'])
                #col1.image(authorImages[idx2], width=200, caption=authors[idx2])
                st.markdown(f'<h2>About {authorNames[idx2+1]}</h2>', unsafe_allow_html=True)
                st.markdown(authorBios[idx2])
                st.markdown(f'To learn more visit their [website]({authorCaption[idx2]}).', unsafe_allow_html=True)
                idx2 = idx2+1 
                st.text("")

    else:
        #if (showBooks == True) & (authorChoice != 'All'): 
      #  filteredImages = bookData[bookData['Author'] == authorChoice]
        authorFiltered = author_df[author_df['Name'] == authorChoice]
        authors = authorFiltered['Name'].unique()
        authorCaption = list(authorFiltered['Website'])
        st.markdown(list(authorFiltered['Bio'])[0])
        for i in range(len(authorFiltered)):
            st.markdown(f'To learn more about {authors[i]}, visit their [website]({authorCaption[i]})', unsafe_allow_html=True)

            # idx = 0
            # for _ in range(len(filteredImages)+1): 
            #     cols = st.beta_columns(4) 
                    
            #     if idx < len(filteredImages): 
            #         cols[0].image(filteredImages[idx], width=150)
                    
            #     idx+=1
                    
            #     if idx < len(filteredImages):
            #         cols[1].image(filteredImages[idx], width=150)
            #     idx+=1

            #     if idx < len(filteredImages):
            #         cols[2].image(filteredImages[idx], width=150)
            #     idx+=1 
            #     if idx < len(filteredImages): 
            #         cols[3].image(filteredImages[idx], width=150)
            #         idx = idx + 1
            #     else:
            #        break

  
