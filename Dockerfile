FROM python:3.9

WORKDIR /wig20-prediction-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

RUN python -m unittest

ENTRYPOINT ["streamlit", "run", "./app/app.py" ]
