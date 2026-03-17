smart-doc-server/
├── server/
│   ├── watcher.py         # monitors upload folder
│   ├── extractor.py       # pdfplumber text extraction
│   ├── embedder.py        # sentence-transformers
│   ├── classifier.py      # train + predict
│   └── api.py             # FastAPI app
├── frontend/
│   └── index.html
├── data/
│   └── labeled/           # your training files
├── models/
│   └── classifier.pkl     # saved trained model
├── requirements.txt
└── README.md