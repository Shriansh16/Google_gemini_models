from dotenv import load_dotenv

load_dotenv()   #loading all the environment variables

import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#functions to load gemini pro models and get responses

model=genai.GenerativeModel("gemini-pro")

def get_gemini_responses(question):
    response=model.generate_content(question)
    return response.text

#initializing streamlit app

st.set_page_config(page_title="qna demo")
st.header("GEMINI LLM APPLICATION")
input=st.text_input('Input: ',key='input')
submit=st.button("ASK THE QUESTION")

if submit:
    response=get_gemini_responses(input)
    st.subheader("THE RESPONSE IS")
    st.write(response)

