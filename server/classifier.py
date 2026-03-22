from sklearn.linear_model import LogisticRegression
import joblib
from extractor import extract_text
from embedder import get_embedding
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # gets you to Local_serv/
DATA_DIR = BASE_DIR / "data"
MODEL_PATH = BASE_DIR / "models" / "classifier.pkl"

categories = ["study", "project", "personal", "finance", "misc"]

def train():
    model = LogisticRegression()
    X = []  # will hold embeddings
    y = []
    for category in categories:
        file_path = DATA_DIR / category  
        for filename in file_path.iterdir():
            if filename.suffix == ".pdf": 
                text = extract_text(filename)
                embedding = get_embedding(text)
                X.append(embedding)
                y.append(category)
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)    

def predict(embedding):
    model = joblib.load(MODEL_PATH)
    return model.predict([embedding])[0]

if __name__ == "__main__":
    train()


