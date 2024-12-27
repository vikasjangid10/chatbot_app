from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import pathlib

import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title='Chatbot for Q%A')
st.header('Chatbot for Q@A')

input = st.text_input("Input :" , key="input")

submit = st.button("Get Response!")

if submit:
    response = get_gemini_response(input)
    st.subheader("the response is :")
    st.write(response)