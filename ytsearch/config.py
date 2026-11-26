import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Path variables for folders
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
VIDEOS_FILE = ROOT_DIR / "videos.txt"
CHUNKS_PATH = DATA_DIR / "chunks.parquet"
EMBEDDINGS_PATH = DATA_DIR / "embeddings.npy"

COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Cohere models
EMBED_MODEL = "embed-v4.0"
RERANK_MODEL = "rerank-v3.5"
CHAT_MODEL = "command-a-03-2025"

# Chunking: about 45 s windows that overlap by 10 s,
# so a sentence cut at a boundary still turns up whole in one chunk
CHUNK_SECONDS = 45
CHUNK_OVERLAP_SECONDS = 10