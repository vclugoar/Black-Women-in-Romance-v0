import streamlit as st 
import itertools 
import pandas as pd 
import numpy as np 
import altair as alt
import matplotlib.pyplot as plt
import time
import seaborn as sns 
from streamlit_embedcode import pastebin_snippet


def app():

    st.title("Methods")
    st.markdown("LDA based recommendation systems for romance novels written by Black women in the romance genre.")

    textProcessingChoices = ["Tokenize", "Remove stopwords", "Stem", "Lemmatize", "Remove proper nouns"]
    with st.beta_container():
        st.markdown(f'<h2>Part 1: Everything about text </h2>', unsafe_allow_html=True)
        
        # get the text section
        st.markdown(f'<h3>1) Get the text </h3>', unsafe_allow_html=True)
        pastebin_snippet("https://pastebin.com/embed_iframe/pRyf4CeQ?theme=white", height=270, width=750)

        # process the text section
        st.markdown(f'<h3>2) Process the text </h3>', unsafe_allow_html=True)
        st.markdown("""
            Multiple ways to process text, each going to give you a different output:
            * Tokenize 
            * Remove stopwords to reduce noise
            * Remove stems to get to the root of the word 
            * Remove lemma to get similar words grouped together
            * Remove proper nouns that would add noise to the data  
        """, unsafe_allow_html=True)

        # process the text -- select box 
        st.markdown(f'<h4>Select processing methods </h4>', unsafe_allow_html=True)
        textUserChoice = st.selectbox("Select a text processing method", textProcessingChoices)

        if textUserChoice == textProcessingChoices[0]:
            pastebin_snippet("https://pastebin.com/UVJrv7zF", height=230, width=750)
        elif textUserChoice == textProcessingChoices[1]:
            pastebin_snippet("https://pastebin.com/XtvRkTyK", height=200, width=750)
        elif textUserChoice == textProcessingChoices[2]:
            pastebin_snippet("https://pastebin.com/PY82TmX2", height=300, width=750)
        elif textUserChoice == textProcessingChoices[3]:
            pastebin_snippet("https://pastebin.com/dVcebeTn", height = 300, width=750)
        elif textUserChoice == textProcessingChoices[4]:
            pastebin_snippet("https://pastebin.com/XSvREUjQ", height=200, width=750)

        st.markdown("Apply created functions:", unsafe_allow_html=True)
        pastebin_snippet("https://pastebin.com/6FDMBKTt", height=200, width=750)
        # gensim 
        st.markdown(f'<h2>Part 2: Gensim implementation of LDA</h2>', unsafe_allow_html=True)
        st.markdown("""
            This section focuses on using Latent Dirichlet Allocation (LDA) to learn yet more about the hidden structure within the 339 romance novels books. LDA is a probabilistic topic model that assumes documents are a mixture of topics and that each word in the document is attributable to the document's topics.

            Info about what is needed for Gensim's implementation. 
        """, unsafe_allow_html=True)
        pastebin_snippet("https://pastebin.com/WYCMkyp0", height=200, width=750)

        # lda spec
        st.markdown(f'<h2>Part 3: Model specifications</h2>', unsafe_allow_html=True)
        st.markdown("""
                LDA model, and get coherence and perplexity score to determine. 
        """, unsafe_allow_html=True)
        pastebin_snippet("https://pastebin.com/zxdASVYc", height=300, width=750)

        st.markdown("My scores were not the highest, actually because my topics use romance novels. Explain how they're different.")

    # with st.beta_container():

    #     document_topic = pd.read_csv("books2.csv")
    #     #bookData = bookData[]
    #    # title('Height vs Weight for Legendary and Non-Legendary Pokemons')
    #     fig = plt.figure()
    #     #sns.set(rc={'figure.figsize':(20,50)})
    #     sns.heatmap(document_topic.loc[document_topic.idxmax(axis=1).sort_values().index], cmap = 'Blues')
    #     st.pyplot(fig)
       

    #     # visualizing results 
    #     st.markdown(f'<h2>Part 4: Visualize Results</h2>', unsafe_allow_html=True)

    #     # interpreting results 
    #     st.markdown(f'<h2>Part 5: Interpret Results</h2>', unsafe_allow_html=True)


#app()


#  source = bookData
#         chart = st.empty()


#         for i in source.index:
#             data_to_be_added = source.iloc[0: i + 1, :]

#             x = alt.Chart(data_to_be_added).mark_circle(size=i * 10).encode(
#                 x='Book',
#                 y='max_col',
#                 color='Book'
#               #  tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
#             ).interactive()

#             time.sleep(0.2)

#             chart.altair_chart(x)