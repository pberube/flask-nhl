# Build
FROM python:3.7 as build

ARG PIP_EXTRA_INDEX_URL

COPY requirements.txt /

WORKDIR /pip-packages

RUN pip download -r /requirements.txt --no-input


# Prod
FROM python:3.7

ENV NHL_SERVICE_ENV=docker

COPY --from=build /pip-packages/ /pip-packages/

RUN pip install --no-index --find-links=/pip-packages/ /pip-packages/*

COPY . /app

WORKDIR /app

#COPY ./docker-entrypoint.sh /

EXPOSE 80

ENTRYPOINT ["python", "/app/app.py"]
CMD ["run"]
