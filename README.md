# YouTube Semantic Search

Semantic search over YouTube transcripts, based on the DeepLearning.AI course
"Large Language Models with Semantic Search": keyword search (BM25), dense
retrieval with Cohere embeddings, reranking, and answers with timestamp citations.

## Setup

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then add your COHERE_API_KEY
```

## Usage

```bash
python scripts/ingest.py        # videos.txt -> data/chunks.parquet
python scripts/build_index.py   # chunks -> data/embeddings.npy
streamlit run app.py
```
