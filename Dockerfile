FROM python:3.11-slim

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt
COPY artifacts/model_trainer/model.joblib /app/artifacts/model_trainer/

CMD ["python3", "app.py"]