from zenml_data.pipelines.training_pipeline import data_validation_pipeline

if __name__ == "__main__":
    pipeline = data_validation_pipeline()
    pipeline.run()
