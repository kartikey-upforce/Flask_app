# Flask_app


This repository contains a Flask web application configured to run in a Docker container. It includes Celery for asynchronous task processing, Redis as the message broker, and Elasticsearch for data indexing and searching.

## Prerequisites

- Docker installed on your machine
- Docker Compose (optional but recommended)

## Setup

1. Clone the repository:

2. Build the Docker images:

3. Start the Docker containers:
Add `-d` flag at the end to run containers in detached mode.

4. Access the Flask app:
Open your web browser and go to `http://localhost:5000/`

## Usage

- Use the `/trigger-task` endpoint to test asynchronous Celery tasks.
- Explore other endpoints for caching data (`/cache-example`), Elasticsearch operations (`/create-index`, `/create-and-search`, `/add-document`, `/search-example`), etc.

## Configuration

- Flask app configurations are set in `config.py`.
- Celery configurations are set in `create_app()` function in `app.py`.
- Redis and Elasticsearch configurations are in `docker-compose.yml`.

## Docker Compose Services

- `app`: Runs the Flask web application.
- `celery-worker`: Executes Celery tasks asynchronously.
- `redis`: Acts as the message broker for Celery.
- `elasticsearch`: Provides data indexing and searching capabilities.

## Development

For development purposes, you can run individual services without Docker Compose:

- Flask app:
- Celery worker:
