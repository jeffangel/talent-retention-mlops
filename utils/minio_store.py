from io import BytesIO, StringIO
import json
import os
import pandas as pd
from typing import Dict, Any

import boto3
from botocore.client import Config

from utils.secret_manager import InfisicalSecretManager

class MinioArtifactStore:
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name
        self.minio_endpoint = os.getenv("S3_ENDPOINT_URL", "http://minio:9000")
        self.minio_config_signature_version = os.getenv("MINIO_CONFIG_SIGNATURE_VERSION", "s3v4")
        self.minio_region_name = os.getenv("MINIO_REGION_NAME", "us-east-1")
        self.secret_manager = InfisicalSecretManager()

    def _create_s3_client(self) -> boto3.client:
        access_key = os.getenv("AWS_ACCESS_KEY_ID") or self.secret_manager.get_secret("MINIO_ACCESS_KEY")
        secret_key = os.getenv("AWS_SECRET_ACCESS_KEY") or self.secret_manager.get_secret("MINIO_SECRET_KEY")
            
        return boto3.client(
                    "s3",
                    endpoint_url = self.minio_endpoint,
                    aws_access_key_id = access_key,
                    aws_secret_access_key = secret_key,
                    config = Config(signature_version=self.minio_config_signature_version),
                    region_name = self.minio_region_name,
                )
    
    def _download_object(self, object_name: str) -> Dict[str, Any]:
        client = self._create_s3_client()
        return client.get_object(Bucket=self.bucket_name, Key=object_name)

    def download_csv(self, object_name: str) -> StringIO:
        response = self._download_object(object_name)
        csv_content = response["Body"].read().decode("utf-8")
        return StringIO(csv_content)

    def download_json(self, object_name: str) -> dict[str, Any]:
        response = self._download_object(object_name)
        json_content = response["Body"].read().decode("utf-8")
        return json.loads(json_content)
    
    def _upload_object(self, object_name: str, data: bytes, content_type: str) -> None:
        client = self._create_s3_client()
        client.put_object(
            Bucket = self.bucket_name,
            Key = object_name,
            Body = data,
            ContentType = content_type
        )

    def upload_csv(self, object_name: str, df: pd.DataFrame) -> None:
        csv_buffer = BytesIO()
        df.to_csv(csv_buffer, index=False)
        self._upload_object(
            object_name = object_name,
            data = csv_buffer.getvalue(),
            content_type = "text/csv"
        )
    def upload_json(self, object_name: str, data: dict[str, Any], indent: int = 2, encode: str = "utf-8") -> None:
        json_data = json.dumps(data, indent=indent, ensure_ascii=False).encode(encode)
        self._upload_object(
            object_name = object_name,
            data = json_data,
            content_type = "application/json"
        )