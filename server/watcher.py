import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from extractor import extract_text
import joblib
from embedder import get_embedding
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "classifier.pkl"
UPLOADS_DIR = BASE_DIR / "uploads"

model = joblib.load(MODEL_PATH)  # Path object works fine with joblib
# rest of your code unchanged


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith(".pdf"):
            time.sleep(1)
            path = event.src_path
            text = extract_text(path)
            embedding = get_embedding(text)
            category = model.predict([embedding])[0]
            print(f"File: {path} → Category: {category}")

folder_to_watch = UPLOADS_DIR

observer = Observer()
observer.schedule(MyHandler(), folder_to_watch, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()