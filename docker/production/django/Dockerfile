FROM python:3.6

ENV PYTHONUNBUFFERED 1

# Install GNU gettext for internationalisation.
RUN apt-get update && apt-get install -y gettext

# Requirements are installed here to ensure they will be cached,
COPY ./django/requirements /requirements
RUN pip install -r /requirements/production.txt

COPY ./docker/production/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/production/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start


COPY ./docker/production/celery/start /start-celeryworker
RUN sed -i 's/\r//' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./docker/production/beat/start /start-celerybeat
RUN sed -i 's/\r//' /start-celerybeat
RUN chmod +x /start-celerybeat


COPY ./django /app
WORKDIR /app

ENTRYPOINT ["/entrypoint"]
