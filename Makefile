build:
	docker compose build

up:
	docker compose up

down:
	docker compose down

debug:
	docker compose run --rm --service-ports api

test:
	docker compose up -d mongo
	docker compose run --rm --service-ports api pytest

test-case:
	docker compose up -d mongo
	docker compose run --rm --service-ports api pytest -k $(TEST)
