# Help using commands
help:
	@echo "Commandes disponibles :"
	@echo "  make docker-up           - Launch the application in detached mode"
	@echo "  make docker-down         - Stop the application"
	@echo "  make docker-logs         - View web container logs"
	@echo "  make docker-shell        - Run a shell in the web container"
	@echo "  make django-migrate      - Apply Django migrations"
	@echo "  make django-superuser    - Create a Django superuser"
	@echo "  make django-startproject - Create a new Django project"
	@echo "  make init                - Initialize the project (launch, migrate, create superuser automatically)"
	@echo "  make up                  - Update and launch the container in detached mode"
	@echo "  make down                - Stop and delete containers"
	@echo "  make stop                - Stop the application"
	@echo "  make start               - Start stopped containers"
	@echo "  make web-logs            - View web container logs"
	@echo "  make web-shell           - Run a shell in the web container"
# Updates the containerup:
up:
	docker compose up --build -d
# Launch the application in detached mode
start:
	docker compose start
	@make web-shell

# Stop the application
stop:
	docker compose stop
# Stop and delete containers
down:
	docker compose down

# Access web container logs
web-logs:
	docker compose logs web

# Run a shell in the web container
web-shell:
	docker compose exec web bash

# Apply Django migrations
django-migrate:
	docker compose exec web python manage.py migrate

# Create a Django superuser
django-superuser:
	docker compose exec web python manage.py createsuperuser

# Create a Django superuser automatically (used by init only)
django-superuser-auto:
	docker compose exec web python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@admin.com', 'adminpass')"

# Create a new Django project
django-startproject:
	docker compose exec web django-admin startproject myproject .

# Initialize the complete project with migrations and superuser
init:
	@make up
	@echo "Attente du démarrage du conteneur..."
	@sleep 10
	@make django-migrate
	@make web-shell
