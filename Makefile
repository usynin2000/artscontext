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

logs_web_app:
	docker-compose -f docker-compose.prod.yml logs web_app

logs_nginx:
	docker-compose -f docker-compose.prod.yml logs nginx

logs_db:
	docker-compose -f docker-compose.prod.yml logs db

lint:
	black .