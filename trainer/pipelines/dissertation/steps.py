from zenml import step

@step
def hello_step() -> None:
    print("✅ Hello from ZenML step!")
