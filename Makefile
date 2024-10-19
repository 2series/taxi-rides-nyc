
# file that contains Make commands for building and running the API

run-dev:
	uvicorn src.main:app --reload --port $${PORT:-8090}

build:
	docker build -t taxi-rides-nyc .

run:
	docker run -p $${PORT:-8090}:8000 taxi-rides-nyc

lint:
	ruff check --fix .

format:
	ruff format .

all: lint format build run

health-check:
	curl -X GET "http://localhost:$${PORT:-8090}/health"

sample-request:
	curl -X GET "http://localhost:$${PORT:-8090}/trips?from_ms=1674561748000&n_results=100"

sample-request-no-results:
	curl -X GET "http://localhost:$${PORT:-8090}/trips?from_ms=1727430298000&n_results=100"

docker-compose-up:
	docker-compose up --build

docker-compose-down:
	docker-compose down