
FROM python:3.7-slim-buster
WORKDIR /application
COPY . /appllication

RUN apt update -y

RUN apt-get update && pip install -r requirements.txt
CMD ["python3", "application.py"]

