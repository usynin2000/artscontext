dev:
	python manage.py runserver

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

up:
	docker compose up --build

down:
	docker-compose down

lint:
	black .
