
# Containers ids
redis-id=$(shell docker ps -a -q -f "name=trvn-redis")
postgres-id=$(shell docker ps -a -q -f "name=trvn-postgres")
django-id=$(shell docker ps -a -q -f "name=trvn-django")
pgadmin-id=$(shell docker ps -a -q -f "name=trvn-pgadmin")


# Build docker containers
build: build-django build-postgres build-redis
build-django:
	@docker-compose -f docker-compose.yml build trvn-django

build-postgres:
	@docker-compose -f docker-compose.yml build trvn-postgres

build-redis:
	@docker-compose -f docker-compose.yml build trvn-redis

build-pgadmin:
	@docker-compose -f docker-compose.yml build trvn-pgadmin

# Start docker containers
start-all:
	@docker-compose up

# Stop docker containers
stop-all:
	@docker-compose stop
stop-redis:
	-@docker stop $(redis-id)
stop-postgres:
	-@docker stop $(postgres-id)
stop-django:
	-@docker stop $(django-id)


# Remove docker containers
rm-all: rm-django rm-postgres rm-redis
rm-redis:
	-@docker rm $(redis-id)
rm-postgres:
	-@docker rm $(postgres-id)
rm-django:
	-@docker rm $(django-id)

# Remove, build and run docker containers
rm-build: stop-all rm-all build run
rm-build-redis: stop-redis rm-redis build-redis
rm-build-postgres: stop-postgres rm-postgres build-postgres
rm-build-django: stop-django rm-django build-django

# Run docker containers
run:
	@docker-compose -f docker-compose.yml up

run-django:
	@docker-compose -f docker-compose.yml up trvn-django


# Go to container bash shell
shell: shell-django

shell-django:
	@docker exec -it trvn-django bash

shell-postgres:
	@docker exec -it trvn-postgres bash

shell-redis:
	@docker exec -it trvn-redis bash


# Django commands
manage:
	@docker exec -t trvn-django python src/manage.py $(cmd)

migrate:
	@docker exec -t trvn-django python src/manage.py migrate

migrations:
	@docker exec -it trvn-django python src/manage.py makemigrations

migrations_merge:
	@docker exec -it trvn-django python src/manage.py makemigrations --merge

superuser:
	@docker exec -it trvn-django python src/manage.py createsuperuser

populatedb:
	@docker exec -it trvn-django python src/manage.py populatedb

# Tests
test:
	@docker exec -t trvn-django /bin/sh -c "cd src && PYTHONDONTWRITEBYTECODE=1 coverage run -m pytest $(dir) --disable-warnings"

coverage:
	@docker exec -t trvn-django /bin/sh -c "cd src && coverage report"

coverage-html:
	@docker exec -t trvn-django /bin/sh -c "cd src && coverage html"

lint:
	@docker exec -t trvn-django /bin/sh -c "cd src && flake8"


build-arm:
	@docker build -f Dockerfile-ARM -t trvn-django:arm .

superuserpre:
	@docker exec -it trvn-django python src/manage.py createsuperuser --username admin --email email@email.email --password password


arm: rm-all build-arm build-pgadmin build-postgres build-redis superuserpre
	@docker-compose -f docker-compose-ARM.yml up

start-arm:
	@docker-compose -f docker-compose-ARM.yml up