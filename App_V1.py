import streamlit as st
#import regex
import yake
from PIL import Image
import streamlit as st
import nltk
import pandas as pd
nltk.download('stopwords')
nltk.download('punkt')
######Headers and Front end Text#########
st.set_page_config(layout="wide")
image = Image.open('pratham-logo.jpeg')
st.image(image, width=500)
st.header("Automatic Tag Generator")
st.markdown(
        """
You can generate automatic tags for your video content using this app.
"""
    )

def hindi_preprocess(text1):
    punc = '''!()-[]{};:।'"\, <>./?@#$%^&*_~'''
    for ele in text1:
        if ele in punc:
            text1=text1.replace(ele, " ")
    hin_stop=pd.read_excel("stopwords_hindi.xlsx",engine='openpyxl')
    stop_hindi=hin_stop['Stopwords'].to_list()
    tokens1 = nltk.word_tokenize(text1)
    tokens_without_stopwords_hindi = [word for word in tokens1 if not word in stop_hindi]
    filtered_text_hindi = (" ").join(tokens_without_stopwords_hindi)
    return filtered_text_hindi

##User Input Text and Language   
user_input = st.text_area('Enter the script')
option = st.selectbox('Please enter Language of your script?',('English', 'Hindi'))

if option=='Hindi':
    max_ngram_size = 1
    kw_extractor = yake.KeywordExtractor(n=max_ngram_size)
    if user_input:
        user_input1=hindi_preprocess(user_input)
        keywords = kw_extractor.extract_keywords(user_input1)
        for i in keywords:
            st.write("#"+i[0])
        
elif option=='English':
    kw_extractor = yake.KeywordExtractor()
    if user_input:
        keywords = kw_extractor.extract_keywords(user_input)
        for i in keywords:
            st.write("#"+i[0])






