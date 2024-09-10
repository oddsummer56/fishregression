from fishregression.model.manager import get_model_path
import pickle
import typer

def run_prediction(length: float):
    
    model_path = get_model_path()
    
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    
    r = model.predict([[length**2, length]])
    
    print(f"length:{length} 물고기는 weight: {r[0]}으로 예측됩니다!")
    return float(r[0])

def predict():
    typer.run(run_prediction)
