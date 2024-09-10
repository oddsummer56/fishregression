import requests
import json

def lr_api(length):

    headers = {
        'accept': 'application/json',
    }

    params = {
        'length': length,
    }

    response = requests.get('http://127.0.0.1:8000/fish_weight', params=params, headers=headers)

    data = json.loads(response.text)
    r = data['prediction']
    
    return r

def kn_api(length, weight):

    headers = {
        'accept': 'application/json',
    }

    params = {
        'length': length,
        'weight': weight,
    }

    response = requests.get('http://localhost:1234/fish', params=params, headers=headers)

    data = json.loads(response.text)
    r = data['prediction']

    return r

def predict():
    length = float(input("물고기 길이(cm) 입력하세요><: "))
    weight = lr_api(length)
    fish = kn_api(length, weight)

    print(f"{length} 물고기의 무게는 {weight} 이고 생선종류는 {fish} 입니다!")
