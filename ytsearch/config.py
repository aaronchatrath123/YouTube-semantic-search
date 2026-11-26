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