# Exercise one and two will be in the init tp folder

# Energy Dashboard Project

This project is a Django application allowing you to visualize energy consumption data by region and by year.

## Features
- Import of energy data via a CSV file. the sample file will be in `init tp/elecConso.csv`.
- Visualization of energy consumption by region and by year.
- REST API to manipulate data (add, update, delete).

## Prerequisites
- [Docker](https://www.docker.com/)
- [Make](https://www.gnu.org/software/make/)

## Facility

Clone this repository:
```bash
git clone https://github.com/afthegamer/test_FS.git
cd test_FS
```

## Launch the Application

Use the `Makefile` to simplify Docker commands.

- To initialize the project with migration:
  ```bash
  make init
  ```
  
- To launch the application in detached mode:
  ```bash
  makeup
  ```

- To apply Django migrations:
  ```bash
  make django-migrate
  ```

- To create a superuser (optional):
  ```bash
  make django-superuser
  ```

## Using the REST API

The API allows you to add, update, and delete energy data.

### Available Endpoints
- **GET** `/energy/api/energy-data/`: Retrieve all energy data.
- **POST** `/energy/api/energy-data/`: Add a new energy entry.
- **PUT** `/energy/api/energy-data/<id>/`: Update an existing entry.
- **DELETE** `/energy/api/energy-data/<id>/`: Delete an entry.

To use the API with tokens:
- Generate an authentication token for a user using:
  ```bash
  docker compose exec web python manage.py drf_create_token <username>
  ```

### Solution 2: Use Token Authentication with Django Rest Framework

If you prefer to secure access to the API (which is generally recommended), you will need to provide an authentication token for POST, PUT, and DELETE requests.

**Install the Django Rest Framework package (if not already done):**
```bash
  pip install djangorestframework
```

**Configure Token Authentication:**
- Add `rest_framework.authtoken` in your `INSTALLED_APPS` in `settings.py`.
- Apply the migrations:
  ```bash
  docker compose exec web python manage.py migrate
  ```

**Create an authentication token for a user:**
- You can create a superuser (if you have not already done so) with:
  ```bash
  docker compose exec web python manage.py createsuperuser
  ```
- Then, generate a token for this user:
  ```bash
  docker compose exec web python manage.py drf_create_token <your_username>
  ```
  Note the generated token.

**Use the Token during the request:** You will need to provide this token for any POST, PUT, or DELETE request. Here is an example of using `curl` with the authentication token:

- **Add a new energy input (POST):**
  ```bash
  curl -X POST http://localhost:8000/energy/api/energy-data/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token <your_token>" \
  -d '{"date": "2024-01-01", "region": "Île-de-France", "consumption_twh": 73.2}'
  ```

- **Update an energy input (PUT):**
  ```bash
  curl -X PUT http://localhost:8000/energy/api/energy-data/1/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token <your_token>" \
  -d '{"date": "2024-01-01", "region": "Île-de-France", "consumption_twh": 74.5}'
  ```

- **Delete an energy entry (DELETE):**
  ```bash
  curl -X DELETE http://localhost:8000/energy/api/energy-data/1/ \
  -H "Authorization: Token <your_token>"
  ```

## Stop the Application
To stop the application, use:
```bash
  make stop
  ```