from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from chatbot import ask_healthcare_agent


app = FastAPI()


# Frontend ko backend se connect karne ke liye
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():

    return {
        "message": "AI Healthcare Assistant is running!"
    }


@app.post("/chat")
def chat(data: dict):

    question = data.get("question", "")

    answer = ask_healthcare_agent(question)

    return {
        "answer": answer
    }