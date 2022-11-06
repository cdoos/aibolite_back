# Aibolite
RESTFul service with Django for maintaining hospital management system.

## Built With

- [Python](https://www.python.org/) 3.6.x
- [Django Rest Framework](http://www.django-rest-framework.org/) 3.8.x

## Installation

Create new directory:

```shell
$ mkdir Aibolite && cd Aibolite
```

Create new virtual environment:

```shell
$ python -m venv venv
```

Activate virtual environment:

```shell
$ source venv/bin/activate  (For Linux)
$ venv/Scripts/activate  (For Windows)
```

Clone this repository:

```shell
$ git clone git@github.com:cdoos/aibolite_back.git && cd aibolite_back/project
```

Install requirements:

```shell
$ pip install -r requirements.txt
```

Check for any project errors:

```shell
$ python manage.py check
```

Run Django migrations to create database tables:

```shell
$ python manage.py migrate
```

Run the development server:

```shell
$ python manage.py runserver
```
