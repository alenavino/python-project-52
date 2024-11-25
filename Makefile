install:
	poetry install

migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

start:
	poetry run python3 manage.py runserver

local:
	poetry run django-admin makemessages --ignore="static" --ignore=".env"  -l ru

translate:
	poetry run django-admin compilemessages

test:
	poetry run python manage.py test

test-coverage:
	poetry run coverage run manage.py test

lint:
	poetry run flake8 task_manager