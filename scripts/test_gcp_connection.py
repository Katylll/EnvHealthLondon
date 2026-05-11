from google.oauth2 import service_account
from google.cloud import bigquery, storage
from config.settings import *

creds = service_account.Credentials.from_service_account_file(KEY_PATH)

bq_client = bigquery.Client(credentials=creds, project=GCP_PROJECT)
gcs_client = storage.Client(credentials=creds, project=GCP_PROJECT)

print("Project:", GCP_PROJECT)
print("Bucket:", GCS_BUCKET)
print("Dataset:", BQ_DATASET)

# Test GCS bucket access
bucket = gcs_client.bucket(GCS_BUCKET)
print("Bucket exists:", bucket.exists())

# Test BigQuery dataset access
dataset_id = f"{GCP_PROJECT}.{BQ_DATASET}"
dataset = bq_client.get_dataset(dataset_id)
print("BigQuery dataset exists:", dataset.dataset_id)

print("✅ GCP connection ready")
