FROM python:3.6-alpine

ENV APP_DIR /app

WORKDIR ${APP_DIR}

COPY . ${APP_DIR}

RUN apk add --no-cache postgresql-libs && \
    apk add --update supervisor &&\
    apk add --no-cache --virtual .build-deps gcc g++ musl-dev postgresql-dev jpeg-dev zlib-dev libffi-dev&&\
    pip install pipenv==2018.11.26 && \
    pipenv install --system --deploy && \
    rm  -rf /tmp/* /var/cache/apk/*

EXPOSE 5000

CMD = ["flask", "run"]
ENTRYPOINT [ "flask", "run" , "--host", "0.0.0.0"]