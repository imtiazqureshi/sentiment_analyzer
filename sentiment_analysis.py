import openai
import streamlit as st
from pathlib import Path
import configparser

openai.api_key = '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'

def get_response_from_chatgpt(text):
    prompt= f"Identify and return the sentiment either positive or negative in given text. text: {text} "
    response= openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a helpful sentiment analyzer that returns concise sentiment"},
            {"role": "user", "content": prompt}
        ],
       temperature=0.1
    )
    sentiment = response['choices'][0]['message']['content']
    return sentiment

st.title("Text Sentiment Analyzer")
model = 'gpt-3.5-turbo'
text = st.text_input("Enter Text: ", value = "e.g. I love to work on AI.")

if st.button('Submit'):
    with st.spinner('Processing your text'):
        sentiment = get_response_from_chatgpt(text)
        st.success('Processing completed')
    # displaying the sentiment to the user
    st.write(f"Sentiment: {sentiment}")
    








