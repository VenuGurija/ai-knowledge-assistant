from fastapi import FastAPI, UploadFile, File
import shutil

from app.rag.pdf_loader import load_pdf
from app.rag.vector_store import create_vector_store
from app.rag.rag_chain import ask_rag

app = FastAPI()

vector_db = None

@app.get("/")
def home():
    return {"message": "AI Knowledge Assistant Running"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    documents = load_pdf(file_path)

    global vector_db
    vector_db = create_vector_store(documents)

    return {
        "message": "PDF uploaded and embeddings created"
    }

@app.get("/ask")
def ask(query: str):

    global vector_db

    if vector_db is None:
        return {"error": "Upload PDF first"}

    answer = ask_rag(vector_db, query)

    return {"response": answer}