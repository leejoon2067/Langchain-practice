# chain.py

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

class DocumentProcessor:
    def __init__(self, pdf_path: str):
        self.loader = PyPDFLoader(pdf_path)
        self.docs = self.loader.load()
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
        self.documents = self.text_splitter.split_documents(self.docs)
    
    def get_documents(self):
        return self.documents


class VectorStore:
    def __init__(self, documents, embedding_model=OpenAIEmbeddings()):
        self.db = FAISS.from_documents(documents, embedding_model)

    def similarity_search(self, query: str):
        return self.db.similarity_search(query)

    def as_retriever(self):
        return self.db.as_retriever()


class LLMModel:
    def __init__(self, model_name: str):
        self.llm = ChatOpenAI(model=model_name)

    def create_prompt(self):
        prompt = ChatPromptTemplate.from_template("""
        Answer the following question based only on the provided context. 
        Think step by step before providing a detailed answer. 
        I will tip you $1000 if the user finds the answer helpful. 
        <context>
        {context}
        </context>
        Question: {input}""")
        return prompt

    def create_document_chain(self, prompt):
        return create_stuff_documents_chain(self.llm, prompt)


class RetrievalChain:
    def __init__(self, retriever, document_chain):
        self.retrieval_chain = create_retrieval_chain(retriever, document_chain)

    def get_response(self, user_input: str):
        response = self.retrieval_chain.invoke({"input": user_input})
        return response
