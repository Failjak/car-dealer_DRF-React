FROM python:3.9-alpine

WORKDIR /django

COPY Pipfile .
COPY Pipfile.lock .
COPY entrypoint.sh /entrypoint.sh

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install pipenv
RUN pipenv install --system --deploy

COPY . .

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]