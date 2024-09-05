dev:
	docker-compose -f docker-compose.dev.yml up --build

down:
	docker-compose -f docker-compose.dev.yml down

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

prod:
	docker-compose -f docker-compose.prod.yml up --build -d


prod_down:
	docker-compose -f docker-compose.prod.yml down


lint:
	black .