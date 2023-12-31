.PHONY: run-dev

run-dev: 
	uvicorn app.api.main:app --reload

.PHONY: migrate-db

migrate-db: 
	alembic revision --autogenerate && alembic upgrade head

.PHONY: test

test:
	python3 -m pytest