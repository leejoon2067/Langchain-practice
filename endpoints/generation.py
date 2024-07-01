# endpoint.py

from typing import Any
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from utils.chain import DocumentProcessor, VectorStore, LLMModel, RetrievalChain

router = APIRouter()

class RequestAnswer(BaseModel):
    question: str

class ResponseAnswer(BaseModel):
    question: str
    llm_answer: str

@router.post("/answer", response_model=ResponseAnswer)
def return_answer(req: RequestAnswer) -> Any:
    pdf_path = "cityfarm_data.pdf"  # PDF 파일 경로
    question = req.question
    
    try:
        # Process the documents
        doc_processor = DocumentProcessor(pdf_path)
        documents = doc_processor.get_documents()
        
        # Create vector store
        vector_store = VectorStore(documents[:30])
        
        # Initialize LLM and create prompt
        llm_model = LLMModel("gpt-turbo-3.5")
        prompt = llm_model.create_prompt()
        
        # Create document chain
        document_chain = llm_model.create_document_chain(prompt)
        
        # Create retrieval chain
        retriever = vector_store.as_retriever()
        retrieval_chain = RetrievalChain(retriever, document_chain)
        
        # Get response
        response = retrieval_chain.get_response(question)
        return {"question": question, "llm_answer": response}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
