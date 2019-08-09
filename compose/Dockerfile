FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

MAINTAINER Andres Orejuela "andresforejuelab@gmail.com"

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add libxml2-dev libxslt-dev python-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi \
  # Translations dependencies
  && apk add gettext

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./compose/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

WORKDIR /app
