def predict():
    length = float(input("물고기의 무게를 입력하세요: "))

    weight = lr_api(length)
    fish_class = knn_api(length, weight)

    print(f"length:{length} 물고기는 weight: {weight}으로 예측 되며 종류는 {fish_class} 입니다")
