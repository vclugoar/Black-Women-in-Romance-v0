import streamlit as st 
import pandas as pd 
import numpy as np 

list_of_h3 = [['Stepping to a New Day','The Kingmaker','The Write Escape: An Irish Romance','His Diamond Queen',
 'Amazing Grace',
 'Something Old',
 'The Rebel King',
 'Taming of Jessi Rose',
 'Measure of a Man',
 'A Sweet Surrender',
 'Sultry in Stilettos',
 'When You Are Mine',
 'Love Takes Time',
 'Surrender to Love',
 'The Bashful Bride',
 'Untamed Love',
 'Make a Scene',
 'Black Dahlia',
 "Love's Sweet Melody",
 'Loving the Lawman',
 'The Pleasure of His Company',
 'The Bewildered Bride',
 'Sinful Chocolate',
 "Destiny's Surrender",
 'Blame It on the Billionaire',
 'No Hiding for The Guilty',
 'This Tender Melody',
 'Something Borrowed',
 'Made to Love',
 'A Duke, the Lady and a Baby',
 'Beauty and the Bachelor',
 "Destiny's Embrace",
 'Every Beat of My Heart',
 'A Hope Divided',
 'Delectable Desire',
 "A Millionaire's Arranged Marriage",
 'His San Diego Sweetheart',
 'The Inheritance',
 'Private Passions',
 'All My Tomorrows',
 "Thorn's Challenge",
 'Home to Wickham Falls',
 'Taken by Storm',
 'A Forever Kind of Love',
 'A Prince on Paper',
 'Love for All Time',
 'Stranded',
 'His Treasure',
 'Mr. Right Next Door',
 'Two to Tango',
 'Secret Vows',
 'Twice the Temptation',
 'Once Ghosted, Twice Shy',
 'Stranger in My Arms',
 'Delicious Destiny',
 'Release Me',
 'A Princess in Theory',
 'Wheels of Steel 4',
 'A Virtuous Ruby',
 'Reckless',
 'Get a Life, Chloe Brown',
 'A Girl Like Her',
 'Hidden Sins',
 'A Treasure of Gold',
 'An Extraordinary Union',
 'Strategic Seduction',
 'Another Chance to Love',
 'Mating the Huntress: A Halloween Romance',
 'Yours Forever',
 'Wellspring',
 "Delaney's Desert Sheikh",
 'Breakaway',
 'Forget Me Not',
 'Her Protector',
 'Betting on Love',
 'More Than He Can Handle',
 'The Edge of Midnight',
 'Royal Holiday',
 'Me and My Boyfriend',
 'His Secret Son',
 'Deception',
 'A Most Precious Pearl',
 'A Love Like This',
 'Body Heat',
 'Through the Storm',
 'A Seal Upon Your Heart',
 'Beautiful & Dirty',
 "Cole's Red Hot Pursuit",
 'Love in Catalina Cove',
 'The Worst Best Man',
 'Negotiating for Love',
 'Secrets and Lies',
 'The Swan',
 'Wild Sweet Love',
 'Comfort of a Man',
 'Business of Love',
 'A San Diego Romance',
 'Electing to Love',
 'Tempest',
 'A Chance with You',
 'Act Your Age, Eve Brown',
 'Slow Burn',
 'Blacker than Blue',
 'A Cowboy to Remember',
 'Stone Cold Surrender',
 'A Little Dare',
 'I Dare You!',
 'Topaz',
 "Couldn't Ask for More",
 "Just Can't Get Enough",
 'A Sultry Love Song',
 'Winds of the Storm',
 "Savannah's Secrets",
 "The Billionaire's Secret",
 'Prima Donna',
 'So Right',
 'American Love Story',
 'Vivid',
 "If It Isn't Love",
 'Back to Your Love',
 'When You Were Mine',
 'Forbidden',
 'Chasing Down a Dream',
 'Someone to Love',
 'The Butterfly Bride',
 'Snowy Mountain',
 'Embracing Forever',
 'The Grunt',
 "Single Mama's Got More Drama",
 'Sultry Pleasure',
 'The Bittersweet Bride',
 'Jack & Diane',
 'Captured',
 'For Your Love: A Blessings Novel',
 'Crystal Clear',
 'Heart of Gold',
 'Loving the Beast',
 'The Nearness of You',
 'Pleasure Under the Sun',
 'A Touch of Love',
 'Indigo',
 'Deadly Sexy',
 'Bring on the Blessings',
 'Something Old, Something New',
 'Hearts on Hold: A Librarian Romance',
 'Unmasked Heart: A Regency Romance',
 'Tempted by You',
 'The Ugly Girlfriend',
 'Affair of Pleasure',
 'Wonder',
 'Night Song',
 'Breathless',
 'Josephine and the Soldier',
 'Before the Dawn',
 'On-Air Passion',
 "Love's Serenade",
 'Belle',
 'Midnight']]



def main(): 
    #bookData = pd.read_csv('books_copy.csv')
    bookData = pd.read_csv('Data/books2.csv')
    bookAuthor = bookData['Author'].unique()
    authors = np.insert(bookAuthor, 0, 'All')
    topics = ['h0', 'h1','h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'h11', 'h12','h13', 'h14', 'h15', 'h16', 'h17', 'h18', 'h19', 'h20', 'h21', 'h22','h23', 'h24', 'h25', 'h26', 'h27', 'h28', 'h29']
    #topics = np.insert(bookTopic, 0, 80)
    year_a = bookData['Year'].unique()
    years = np.insert(year_a, 0, 0)
    years.sort()

    #st.markdown(f'<h2>Use filters by topic and author or scroll down to explore the books used to build the LDA-based recommendation system</h3>', unsafe_allow_html=True)
    st.subheader('Use filters by topic and author or scroll down to explore the books used to build the LDA-based recommendation system')
    
    box1, box2 = st.beta_columns(2)
    authorChoice = box1.selectbox('Filter by author:', authors, format_func=lambda x: 'Filter by author' if x == '' else x, key='All')
    topicChoice = st.multiselect('Filter by topic:', topics, format_func=lambda x: 'Filter by topic' if x == '' else x)
    yearChoice = box2.selectbox('Filter by year:', years, format_func=lambda x: 'Filter by topic' if x == '' else x)
    descriptionChoiceC = st.checkbox('Show book descriptions', value=False)

    st.write(topicChoice)
    st.write(len(topicChoice))
   # st.write(topicChoice[0])
    st.markdown(f'Books written by {authorChoice}, with the topic {topicChoice}',
        unsafe_allow_html=True)

    if (authorChoice == 'No') & (yearChoice == 0) & (len(topicChoice) == 0):
       st.image('https://i.ibb.co/X3Dpz54/Use-the-filters-above-to-see-books-2.png', use_column_width=True)
    else: 
        bookFiltered = bookData[((bookData['Author'] == authorChoice)) | (bookData['Year'] == yearChoice)]
        if 'h3' in topicChoice:
            st.write(list_of_h3)

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
                

main()