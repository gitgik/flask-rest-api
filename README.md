# flask-rest-api [![Build Status](https://travis-ci.org/gitgik/flask-rest-api.svg?branch=master)](https://travis-ci.org/gitgik/flask-rest-api)

A flask-driven restful API for Bucketlist interactions

## Technologies used

* **[Python3](https://www.python.org/downloads/)** - A programming language that lets you work more quickly (The universe loves speed!).
* **[Flask](flask.pocoo.org/)** - A microframework for Python based on Werkzeug, Jinja 2 and good intentions
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - A tool to create isolated virtual environments
* **[PostgreSQL](https://www.postgresql.org/download/)** – Postgres database offers many [advantages](https://www.postgresql.org/about/advantages/) over others.
* Minor dependencies can be found in the requirements.txt file on the root folder.

## Installation / Usage

* If you wish to run your own build, first ensure you have python3 globally installed in your computer. If not, you can get python3 [here](https://www.python.org).
* After this, ensure you have installed virtualenv globally as well. If not, run this:

    ```bash
    pip install virtualenv
    ```

* Git clone this repo

    ```bash
    git clone git@github.com:gitgik/flask-rest-api.git
    ```

* ### Dependencies

    1. Cd into your the cloned repo:

        ```bash
        cd flask-rest-api
        ```

    2. Create and get into your virtual environment:

        ```bash
        virtualenv -p python3 venv
        source venv/bin/activate
        ```

* ### Environment Variables

    Install [Dotenv](https://pypi.org/project/python-dotenv/) as follows:

    ```bash
    pip install python-dotenv
    ```

    Create a .env file and add the following:

    ```bash
    SECRET="some-very-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING"
    APP_SETTINGS="development"
    DATABASE_URL="postgresql://localhost/flask_api"
    ```

    Dotenv will load your environment variables by reading the key-value pairs from the .env file.

* ### Install your requirements
  
    ```bash
    (venv)$ pip install -r requirements.txt
    ```

* ### Database Migrations

    Make sure your postgresql server is running. Then, on your psql console, create your database:

    ```bash
    $ psql -U postgres
    > CREATE DATABASE flask_api;
    ```

    In the project directory, make and apply your Migrations

    ```bash
    (venv)$ flask db init

    (venv)$ flask db migrate
    ```

    And finally, migrate to persist them on the database

    ```bash
    (venv)$ flask db upgrade
    ```

* ### Running the Server

    On your terminal, run the server using this one simple command:

    ```bash
    (venv)$ flask run
    ```

    You can now access the app on your local browser by using

    ```bash
    http://localhost:5000/bucketlists/
    ```

    Or test creating bucketlists using Postman
