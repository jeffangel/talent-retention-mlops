from zenml import pipeline
from zenml_data.steps.data_validator import validate_data

@pipeline
def data_validation_pipeline():
    validate_data()
