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

upgrade:
	docker compose run api alembic upgrade head

downgrade:
	docker compose run api alembic downgrade base

alembic:
	docker compose run api alembic revision --autogenerate -m "$(MIGRATION)"

test-case:
	docker compose up -d mongo
	docker compose run --rm --service-ports api pytest -k $(TEST)
