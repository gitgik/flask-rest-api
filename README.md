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
    ```
        $ pip install virtualenv
    ```
* Git clone this repo to your PC
    ```
        $ git clone git@github.com:gitgik/flask-rest-api.git
    ```


* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```
        $ cd flask-rest-api
        ```

    2. Create and fire up your virtual environment in python3:
        ```
        $ virtualenv -p python3 venv
        $ pip install autoenv
        ```

* #### Environment Variables
    Create a .env file and add the following:
    ```
    source venv/bin/activate
    export SECRET="some-very-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING"
    export APP_SETTINGS="development"
    export DATABASE_URL="postgresql://localhost/flask_api"
    ```

    Save the file. CD out of the directory and back in. `Autoenv` will automagically set the variables.
    We've now kept sensitive info from the outside world! 😄

* #### Install your requirements
    ```
    (venv)$ pip install -r requirements.txt
    ```

* #### Migrations
    On your psql console, create your database:
    ```
    > CREATE DATABASE flask_api;
    ```
    Then, make and apply your Migrations
    ```
    (venv)$ python manage.py db init

    (venv)$ python manage.py db migrate
    ```

    And finally, migrate your migrations to persist on the DB
    ```
    (venv)$ python manage.py db upgrade
    ```

* #### Running It
    On your terminal, run the server using this one simple command:
    ```
    (venv)$ flask run
    ```
    You can now access the app on your local browser by using
    ```
    http://localhost:5000/bucketlists/
    ```
    Or test creating bucketlists using Postman
