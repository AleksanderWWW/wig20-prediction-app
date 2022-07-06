FROM python:3.9

WORKDIR /wig20-prediction-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

EXPOSE 8501

CMD ["streamlit", "run", "./app/app.py" ]
