from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])

def get_response(msg):
    response=chat.send_message(msg,stream=True)
    return response

#initializing streamlit app
st.set_page_config(page_title="Chat Here")
st.header("Gemini LLM application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("click here")
if submit and input:
    response=get_response(input)
    #adding user's query and response to the session
    st.session_state['chat_history'].append(('you',input))
    st.subheader("The response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(('bot',chunk.text))
st.subheader("The Chat History is")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")