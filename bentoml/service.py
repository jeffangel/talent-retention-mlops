import bentoml
import numpy as np
import joblib
from bentoml.exceptions import NotFound

model_path = "model.joblib"
model_name = "production"

try:
    bentoml.models.get(f"{model_name}:latest")
except NotFound:
    model = joblib.load(model_path)
    bentoml.sklearn.save_model(model_name, model)

loaded_model = bentoml.sklearn.load_model(f"{model_name}:latest")

svc_production = bentoml.Service(name=model_name)

@svc_production.api(input=bentoml.io.JSON(), output=bentoml.io.JSON())
def predict(data):
    prediction = loaded_model.predict(np.array(data["x"]).reshape(1, -1))
    return {"result": prediction.tolist()}
