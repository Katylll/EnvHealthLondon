import os

# Google Cloud settings
GCP_PROJECT = "env-health-london-2026"
GCP_REGION = "europe-west2"

# Storage
GCS_BUCKET = "env-health-london-data-2026-katy"

# BigQuery
BQ_DATASET = "env_health"
BQ_TABLE_MAIN = f"{GCP_PROJECT}.{BQ_DATASET}.master_borough"
BQ_TABLE_EBS = f"{GCP_PROJECT}.{BQ_DATASET}.ebs_results"
BQ_TABLE_DID = f"{GCP_PROJECT}.{BQ_DATASET}.did_results"

# AI / RAG settings
OPENAI_MODEL = "gpt-4o-mini"
EMBED_MODEL = "all-MiniLM-L6-v2"
CHROMA_PATH = "./chromadb"

# Local project paths
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
FIGURES_DIR = os.path.join(PROJECT_ROOT, "figures")
SECRETS_DIR = os.path.join(PROJECT_ROOT, "secrets")

# Service account key path
KEY_PATH = os.path.join(SECRETS_DIR, "gcp_key.json")
