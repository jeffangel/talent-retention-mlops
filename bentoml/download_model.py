import os
import boto3

endpoint_url = "http://minio:9000"
access_key = os.environ["MINIO_ACCESS_KEY"]
secret_key = os.environ["MINIO_SECRET_KEY"]
bucket = "artifacts"
object_key = "builder/production/model.joblib"
destination = os.path.join(os.path.dirname(__file__), "model.joblib")

os.makedirs("bentoml", exist_ok=True)

client = boto3.client(
    "s3",
    endpoint_url=endpoint_url,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)

print(f"Downloading {object_key} from MinIO...")
client.download_file(bucket, object_key, destination)
print(f"Saved in {destination}")
