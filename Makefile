dev:
	docker-compose -f docker-compose.dev.yml up --build

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

prod:
	docker-compose -f docker-compose.prod.yml up --build

down:
	docker-compose down

lint:
	black .