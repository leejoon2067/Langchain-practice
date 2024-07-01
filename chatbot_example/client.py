import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/topic_example/invoke",
    json = {'input' : {'topic' : input_text}})

    return response.json()['output']['content']

st.title('Langchain Demo With GPT')
input_text = st.text_input("원하는 주제의 질문을 하세요.")

if input_text: 
    st.write(get_openai_response(input_text))