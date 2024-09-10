from typing import Union
from fastapi import FastAPI
from fishregression.model.manager import get_model_path
import pickle

app = FastAPI()

def load_model():
    model_path = get_model_path()

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    return model

@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/fish_weight")

def fish(length: float):
    """
    물고기 길이로 무게 예측하기

    Args:
        length (float): 물고기 길이(cm)

    Returns:
        weight: 물고기 길이에 따라 예측된 무게
    """
    model = load_model()
    prediction = model.predict([[length**2, length]])

    return {
                "length": length,
                "prediction": prediction[0],
            }
