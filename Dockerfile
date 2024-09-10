#BASE 이미지 시작점
FROM oddsummer/fishmlserv:1.0.1

WORKDIR /code

COPY src/fishregression/main.py /code/

# 모델서빙만(의존성은 위 BASE 이미지에서 모두 설치했다)
RUN pip install --no-cache-dir --upgrade git+https://github.com/oddsummer56/fishregression.git@0.3.1

# 모델 서빙을 위해 API 구동을 위한 FastAPI RUN
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
