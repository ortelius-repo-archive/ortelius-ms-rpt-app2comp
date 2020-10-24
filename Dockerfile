FROM tiangolo/meinheld-gunicorn-flask:python3.8-alpine3.11
#ENV PYTHONUNBUFFERED True
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
#EXPOSE 5000
#CMD ["waitress-serve","--port=5000", "app2comp:app"]
