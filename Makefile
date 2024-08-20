# Setup virtualenv
deps:
	./scripts/deps.sh

# Start Virtualenv
activate:
	pipenv shell

# Update requirements.txt and requirements-dev.txt (run after installing or updating a package)
freeze:
	pipenv requirements > requirements.txt; pipenv requirements --dev-only > requirements-dev.txt

# Build all services in parallel
build:
	docker-compose build --parallel

# Bring all the service containers up in the correct order.
up:
	docker-compose up -d

# Bring down all containers
down: 
	docker-compose down

# Logs for all containers
logs:
	docker-compose logs -f