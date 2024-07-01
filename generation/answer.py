from langchain.chat_models import ChatOpenAI

from core.config import settings
from generation.prompt import answer_prompt_template

def return_answer(question):
    chat = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0,
            openai_api_key=settings.OPENAI_API_KEY,
        )
    prompt = answer_prompt_template.format(question=question)
    response = chat.predict(prompt)
    return response