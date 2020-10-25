FROM tiangolo/meinheld-gunicorn-flask:python3.8-alpine3.11
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
