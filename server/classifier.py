from sklearn.linear_model import LogisticRegression
import joblib
from extractor import extract_text
from embedder import get_embedding
import os

model = LogisticRegression()
X = []  # will hold embeddings
y = []  # will hold labels

categories = ["study", "project", "personal", "finance", "misc"]

for category in categories:
    folder_path = os.path.join(r"C:\Users\akash\Documents\Local_serv\data", category)
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename) 
            text = extract_text(file_path)
            embedding = get_embedding(text)
            X.append(embedding)
            y.append(category)

model.fit(X, y)
joblib.dump(model, r"C:\Users\akash\Documents\Local_serv\models\classifier.pkl")


