FROM python:3.9.14-slim-bullseye
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/

RUN apt-get update

RUN apt-get install  \
    ca-certificates gcc libpq-dev musl-dev \
    libffi-dev curl cargo -y

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ADD . /code/

CMD gunicorn trvn_appbackend.wsgi:application --log-file - --bind 0.0.0.0:8001