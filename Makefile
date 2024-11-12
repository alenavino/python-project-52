install:
	poetry install

migrate:
	python manage.py makemigrations
	python manage.py migrate

start:
	python3 manage.py runserver

local:
	poetry run django-admin makemessages --ignore="static" --ignore=".env"  -l ru

translate:
	poetry run django-admin compilemessages
