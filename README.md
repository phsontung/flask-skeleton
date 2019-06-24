# WIP: flask-skeleton

## What's included?

|Module|Package|Description|
|:-----|:------|:----------|
|Database    |[Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)||
|Database migration|[Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)||
|Authentication|[Flask-Login](https://flask-login.readthedocs.io/en/latest/)||
|Flask WTFForm|https://flask-wtf.readthedocs.io/en/stable/||
|Email|[Flask-Mail](https://pythonhosted.org/Flask-Mail/)||
|Restful API|[Flask-Restful](https://flask-restful.readthedocs.io/en/latest/)||
|Flask Caching|[Flask-caching](https://flask-caching.readthedocs.io/en/latest/)||
|JWT Authentication|[Flask-JWT-Entended](https://flask-jwt-extended.readthedocs.io/en/latest/)||
|Hash Password|[Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)||
|Redis|[Flask-redis](https://pypi.org/project/flask-redis/)||
|Celery|http://flask.pocoo.org/docs/1.0/patterns/celery/||
|AMQP| [Pika](https://www.rabbitmq.com/tutorials/tutorial-one-python.html) |Working with RabbitMQ |
|Testing|[Pytest](https://docs.pytest.org/en/latest/)||
|Apply Middleware|||
|uwsgi|||
|Traefik|||
|HTTPS/SSL|Let's Encrypt||
|Kubernetes|||
|Sentry|https://sentry.io/for/flask/||
|Docker|||
|docker-compose||
|SMTP Mail Server|mailcatcher|Fake smtp email server for testing email|

## How it works?

- Celery was used for sending email in async fashion

## Let's get start
- Clone source code
```bash
git clone https://gitlab.com/mekongsmartcam/engine/flask-skeleton
```

### Work with docker-compose
- Build flaskapp
```
docker-compose build flaskapp
```
- Run flask application
```
docker-compose up
```

### Run flaskapp in local virtual environment
- Install pipenv for working with Pipfile and virtualenv
```
pip install pipenv
```

- Change directory to flask-skeleton and install dependencies
```
pipenv install --dev
```

- Create `.env` file (flask environment variables)
```
# Flask built-in environment variables
FLASK_ENV=development
SERVER_NAME=0.0.0.0
FLASK_APP=app.py
FLASK_DEBUG=1

# User define environmnet variables
FLASK_APP_ENV=dev
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_USERNAME=test
DATABASE_PASSWORD=test
DATABASE_NAME=test
```

- Activate virtualenv
```
pipenv shell
```

- Run flask application
```
# flash run

 * Serving Flask app "app.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 206-413-235
```

- Note: In case you run with postgresql, you can use docker-compose to run postgresql only (+ mailcatcher if need)
```
docker-compose up postgres mailcatcher
```


## References

- [Structure of Flask application](https://lepture.com/en/2018/structure-of-a-flask-project)
- [Authentication and Authorization with Flask-Login](https://scotch.io/tutorials/authentication-and-authorization-with-flask-login)
- [Cookiecutter-flask](https://github.com/cookiecutter-flask/cookiecutter-flask)
- [Token based authentication with flask](https://realpython.com/token-based-authentication-with-flask/)
- [Docker container for flask micro service](https://github.com/AmeyRuikar/D-Flask)
- [Swagger UI](https://towardsdatascience.com/working-with-apis-using-flask-flask-restplus-and-swagger-ui-7cf447deda7f)

## Wanna help?
- Create pull requests if you can bring something cool (constructive)
- Create issues if you feel something wrong

# TODO
- Add Travis CI: https://travis-ci.org
- Add code coverage: https://codecov.io
- Add code climate: https://codeclimate.com
- Pyup.io: https://pyup.io/
- Reload flask app and install pip packages when running with docker-compose
