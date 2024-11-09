FILE ?= docker_compose/app.yaml

up:
	docker-compose -f $(FILE) up

down:
	docker-compose -f $(FILE) down