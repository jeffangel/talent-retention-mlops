from zenml.steps import step
from zenml.config import DockerSettings
from zenml.client import Client

docker_settings = DockerSettings(
    requirements=["pandas", "great_expectations", "pandera", "boto3", "infisical-sdk"],
    environment={
        "AWS_ACCESS_KEY_ID": "nf7n2MunJE57CnJfv9sd",
        "AWS_SECRET_ACCESS_KEY": "MkDK1Ktinra5I9j0FVbB98kW4sE1fTDSZgnGbw07",
        "AWS_REGION": "us-east-1",
        "S3_ENDPOINT_URL": "http://minio:9000"
    }
)

@step(settings={"docker": docker_settings})
def validate_data() -> None:
    import os
    print("KEY_ID:", os.getenv("AWS_ACCESS_KEY_ID"))
    print("SECRET:", os.getenv("AWS_SECRET_ACCESS_KEY"))
    print("ENDPOINT:", os.getenv("S3_ENDPOINT_URL"))

    from datetime import datetime
    import great_expectations as ge
    import logging
    import pandas as pd
    from pandera import Column, DataFrameSchema, Check
    
    from utils.minio_store import MinioArtifactStore
    
    logger = logging.getLogger(__name__)

    bucket_name = "datasets"
    object_name = "bronze/latest/WA_Fn-UseC_-HR-Employee-Attrition.csv"
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    minio_client = MinioArtifactStore(bucket_name)
    
    csv = minio_client.download_csv(object_name=object_name)
    df = pd.read_csv(csv)
    gdf = ge.from_pandas(df)

    experiment_tracker = Client().active_stack.experiment_tracker
    with experiment_tracker.run_step(name="validate_data") as experiment:
        experiment.log_other("object_name", object_name)
        experiment.log_other("timestamp", timestamp)
        experiment.log_metric("n_rows", df.shape[0])
        experiment.log_metric("n_columns", df.shape[1])

        gdf.expect_column_to_exist("Age")
        gdf.expect_column_values_to_not_be_null("Age")
        gdf.expect_column_values_to_be_between("Age", min_value=18, max_value=65)
        gdf.expect_column_to_exist("Attrition")
        gdf.expect_column_values_to_be_in_set("Attrition", ["Yes", "No"])

        results = gdf.validate()
        experiment.log_metric("validation_success", int(results.success))
        
        if not results.success:
            experiment.log_text("Fallback schema (Pandera) applied due to GE failure.")
            schema = DataFrameSchema({
                "Age": Column(int, Check.in_range(18, 65), nullable=False),
                "Attrition": Column(str, Check.isin(["Yes", "No"]))
            })
            df = schema.validate(df)
        else:
            experiment.log_text("GE validation passed. No fallback needed.")
        
        try:
            for version in ["latest", timestamp]:
                minio_client.upload_csv(
                    object_name="bronze/validated/{}_WA_Fn-UseC_-HR-Employee-Attrition.csv".format(version),
                    df=df
                )
        except Exception as e:
            logger.error(f"Failed to upload validated data: {e}")
            experiment.log_text(f"Upload failed: {e}")
