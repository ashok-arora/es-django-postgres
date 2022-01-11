# commands.md

## Setting up postgresql on macOS
brew services start postgresql

psql postgres
CREATE ROLE testuser WITH LOGIN PASSWORD '123';
ALTER ROLE testuser CREATEDB;

psql postgres -U testuser
create database testdb;

## django server
pipenv run python manage.py makemigrations images
pipenv run python manage.py migrate images

pipenv run python manage.py createsuperuser
pipenv run python manage.py runserver 8080

## elasticsearch setup and indexing
pipenv run python -m pip install git+https://github.com/django-es/django-elasticsearch-dsl.git

pipenv run python manage.py search_index --rebuild