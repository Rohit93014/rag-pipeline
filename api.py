# from fastapi import FastAPI
# from pydantic import BaseModel

# from rag import get_answer

# app = FastAPI()

# class QueryRequest(BaseModel):
#     query: str

# @app.get("/")
# def home():
#     return {"message": "RAG API Running"}

# @app.post("/ask")
# def ask_question(request: QueryRequest):
#     answer = get_answer(request.query)

#     return {
#         "query": request.query,
#         "answer": answer
#     }




from fastapi import FastAPI
from pydantic import BaseModel

from rag import get_answer

app = FastAPI(
    title="RAG API",
    version="1.0"
)

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {
        "message": "RAG API Running Successfully"
    }

@app.post("/ask")
def ask_question(request: QueryRequest):

    answer = get_answer(request.query)

    return {
        "query": request.query,
        "answer": answer
    }