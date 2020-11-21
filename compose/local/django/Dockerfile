
FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1
ENV PYCURL_SSL_LIBRARY=openssl

RUN apt-get update \
  # psycopg2 dependencies
  && apt-get install -y build-essential gcc musl-dev libpq-dev \
  # Encryption dependencies
  && apt-get install -y libffi-dev python-cffi gnupg \
  # Translations dependencies
  && apt-get install -y gettext \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  && apt-get install -y postgresql-client \
  # project dependencies
  && apt-get install -y git libssl-dev libcurl4-openssl-dev


COPY ./compose/common/entrypoint /entrypoint
COPY ./compose/common/django/pm /usr/local/bin/pm
COPY ./compose/local/django/start /start
COPY ./compose/local/django/test /usr/local/bin/test

RUN sed -i 's/\r$//g' /entrypoint && chmod +x /entrypoint && \
  sed -i 's/\r$//g' /start && chmod +x /start && \
  sed -i 's/\r$//g' /usr/local/bin/pm && chmod +x /usr/local/bin/pm && \
  sed -i 's/\r$//g' /usr/local/bin/test && chmod +x /usr/local/bin/test


# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

RUN apt-get purge -y --auto-remove build-essential gcc

WORKDIR /app

ENTRYPOINT ["/entrypoint"]