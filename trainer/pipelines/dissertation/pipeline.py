from zenml import pipeline
from steps import hello_step

@pipeline
def hello_world_pipeline():
    hello_step()

if __name__ == "__main__":
    hello_world_pipeline()