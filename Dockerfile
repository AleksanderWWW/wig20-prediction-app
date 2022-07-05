FROM python:3.10

WORKDIR /wig20-prediction-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD [ "streamlit", "run", "./app/app.py" ]
