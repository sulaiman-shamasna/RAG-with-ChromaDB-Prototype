# backend_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chatbot import RAGChatbot
from retriever import Retriever
import uvicorn
import os

app = FastAPI(title="Ollama RAG Chatbot API")

class ChatRequest(BaseModel):
    query: str

retriever = Retriever()
chatbot = RAGChatbot(retriever, model_name='llama2')  # Replace 'llama2' with your model name

@app.post("/chat", summary="Generate chatbot response")
async def chat(request: ChatRequest):
    user_query = request.query.strip()
    if not user_query:
        raise HTTPException(status_code=400, detail="No query provided.")

    response = chatbot.generate_response(user_query)
    return {"response": response}

if __name__ == '__main__':
    if not 'OLLAMA_HOME' in os.environ:
        print("Warning: 'OLLAMA_HOME' environment variable is not set. Ensure Ollama is installed correctly.")
    uvicorn.run(app, host="0.0.0.0", port=8000)
