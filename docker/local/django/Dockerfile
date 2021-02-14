FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install GNU gettext for internationalisation.
RUN apt-get update && apt-get install -y gettext

# Install gdal for geodjango
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin

# Requirements are installed here to ensure they will be cached,
COPY ./django/requirements /requirements
RUN pip install -r /requirements/local.txt

COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start


COPY ./docker/local/celery/start /start-celeryworker
RUN sed -i 's/\r//' /start-celeryworker
RUN chmod +x /start-celeryworker


WORKDIR /app

RUN sed -i 's/{% load staticfiles %}/{% load static %}/g' /usr/local/lib/python3.6/site-packages/rest_framework_swagger/templates/rest_framework_swagger/index.html

ENTRYPOINT ["/entrypoint"]
