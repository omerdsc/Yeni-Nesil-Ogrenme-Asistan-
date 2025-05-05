# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.rag_pipeline import ask_with_rag  
from fastapi import File, UploadFile
import shutil


def mock_answer(question: str) -> str:
    return f"'{question}' sorusu için örnek bir cevap burada olacak."


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Geliştirme aşamasında açık bırakıyoruz
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Question(BaseModel):
    user_input: str



@app.post("/ask")
def ask_question(q: Question):
    response = ask_with_rag(q.user_input)
    return {"answer": response}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = "app/data/sample_notes.txt"
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"message": "File uploaded successfully"}
