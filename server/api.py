from fastapi import FastAPI, UploadFile, File
from pathlib import Path
import shutil
import sys

sys.path.append(str(Path(__file__).resolve().parent))

from extractor import extract_text
from embedder import get_embedding
from classifier import predict



BASE_DIR = Path(__file__).resolve().parent.parent
UPLOADS_DIR = BASE_DIR / "uploads"
MODEL_PATH = BASE_DIR / "models" / "classifier.pkl"
UPLOADS_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI()

@app.get("/status")
def status():
    return {"status": "ok"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    destination = UPLOADS_DIR / file.filename
    with open(destination, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"filename": file.filename}

@app.post("/classify/{filename}")
def classify_file(filename: str):
    file_path = UPLOADS_DIR / filename
    text = extract_text(file_path)
    embedding = get_embedding(text)
    category = predict(embedding)
    return {"filename": filename, "category": category}