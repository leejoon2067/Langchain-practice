from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os

from dotenv import load_dotenv
load_dotenv()


# 인도 아재 예제
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "넌 친절한 인공지능 도우미야. 입력된 query에 따라 한글로 대답을 해주면 돼."),
        ("user", "질문: {Question}")
    ]
)

st.title("langchain practice llm")
input_text = st.text_input("원하는 주제의 질문을 하세요.")

llm = ChatOpenAI(model_name="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'Question' : input_text}))


# teddynote 예제

#llm = ChatOpenAI(
#    temperature = 0.5,
#    model_name="gpt-3.5-turbo",  # 모델명
#)

# 질의내용
# question = "대한민국의 수도는 어디인가요?"

# 질의
# print(f"[답변]: {llm.invoke(question)}")

# answer = llm.stream("대한민국의 아름다운 경치 10곳과 주소를 알려주세요")

# for token in answer: 
#    print(token.content, end = "", flush = True)
