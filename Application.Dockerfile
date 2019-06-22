FROM python:3.6-alpine

ENV APP_DIR /app
ENV PYTHONPATH=/app

WORKDIR ${APP_DIR}

COPY . ${APP_DIR}
COPY deployment/docker/Application/conf/uwsgi.ini ${APP_DIR}/uwsgi.ini

RUN apk add --no-cache postgresql-libs && \
    apk add --update supervisor &&\
    apk add --no-cache --virtual .build-deps gcc g++ musl-dev postgresql-dev jpeg-dev zlib-dev libffi-dev&&\
    pip install pipenv==2018.11.26 && \
    pipenv install --system --deploy && \
    rm -rf /tmp/* /var/cache/apk/*

EXPOSE 5000

CMD ["uwsgi", "--ini", "/app/uwsgi.ini"]
