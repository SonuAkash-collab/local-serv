import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from extractor import extract_text
import joblib
from embedder import get_embedding

model = joblib.load(r"C:\Users\akash\Documents\Local_serv\models\classifier.pkl")


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith(".pdf"):
            time.sleep(1)
            path = event.src_path
            text = extract_text(path)
            embedding = get_embedding(text)
            category = model.predict([embedding])[0]
            print(f"File: {path} → Category: {category}")

folder_to_watch = r"C:\Users\akash\Documents\Local_serv\uploads"

observer = Observer()
observer.schedule(MyHandler(), folder_to_watch, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()