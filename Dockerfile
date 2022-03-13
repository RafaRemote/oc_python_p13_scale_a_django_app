FROM python:3.9.2-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

ADD . .


ENV PORT=8000

CMD python manage.py runserver 0.0.0.0:$PORT