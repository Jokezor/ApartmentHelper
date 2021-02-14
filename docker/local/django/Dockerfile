FROM python:3.6

ENV PYTHONUNBUFFERED 1

# Install GNU gettext for internationalisation.
RUN apt-get update && apt-get install -y gettext

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

ENTRYPOINT ["/entrypoint"]
