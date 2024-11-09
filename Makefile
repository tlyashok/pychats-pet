DEV_DC = -f docker_compose/dev/docker-compose.yaml
ENV = --env-file .env
APP_CONTAINER = main_app


up:
	docker-compose $(DEV_DC) $(ENV) up

down:
	docker-compose $(DEV_DC) $(ENV) down

env:
	copy .env.example .env

shell:
	docker exec -it $(APP_CONTAINER) bash
