# without Docker

run:
	streamlit run .\app\app.py

setup: requirements.txt
	python -m virtualenv venv
	venv\Scripts\activate
	pip install -r requirements.txt


# with Docker

build-docker: Dockerfile
	docker build -t wig20-prediction-app .

run-new-docker:
	docker run --name wig20-app wig20-prediction-app

run-existing-docker:
	docker start wig20-app

stop-docker:
	docker stop wig20-app