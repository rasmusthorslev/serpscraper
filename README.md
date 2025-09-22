# RankTracker

A Python 3.13 web application for tracking Google search ranks for keywords associated with clients. Uses Django (views + ORM), Playwright + Playwright Stealth for scraping, PostgreSQL for data storage, and Celery for async tasks. Deployed and run via Docker.

## Features

- **Django Admin** for managing clients and keywords
- **Scraper**: Uses Playwright and Playwright Stealth to collect Google search rank data
- **ORM**: Keywords linked to one or more clients; rank results stored per keyword and domain
- **PostgreSQL**: Database for all persistent data
- **Celery**: For potential background scraping tasks (can be extended)
- **Dockerized**: Easy setup and reproducibility

## Requirements

- Python 3.13
- Django >= 4.2
- asgiref >= 3.4.0
- playwright
- playwright_stealth
- psycopg2-binary
- celery

All dependencies should be listed in `requirements.txt`.

## Setup

1. **Clone the repo**

    ```bash
    git clone <repo-url>
    cd ranktracker
    ```

2. **Configure environment variables**

   - Create your own `.env` file (see `.env.example` if present) and set variables for Django, database, and any other required secrets.
   - The Docker Compose file is set up to load variables from `.env`.

3. **Build and run with Docker Compose**

    ```bash
    docker compose up --build
    ```

4. **Apply migrations**

    ```bash
    docker compose exec web python manage.py migrate
    ```

5. **Create a superuser (for Django admin)**

    ```bash
    docker compose exec web python manage.py createsuperuser
    ```

## Scraping Google Search Results

The main scraping script is located at `core/scraper.py`. By default, it scrapes all saved keywords.

**Execute the scraper:**

```bash
docker compose exec web python core/scraper.py
```

- The script will use Playwright with Stealth mode to fetch Google search results for each keyword.
- Results are saved in the database and linked to keywords (and thus clients).

You can filter results for a specific client or keyword via Django ORM or admin interface.

## Customization

- **Filter scraping for a specific client:**  
  Adapt `core/scraper.py` to only process keywords associated with a particular client using Django ORM filtering.
- **Celery integration:**  
  Extend scraping to run asynchronously or periodically using Celery (see `celery.py` and tasks).

## Useful Docker Compose commands

- Run Django shell:  
  ```bash
  docker compose exec web python manage.py shell
  ```
- Collect static files:  
  ```bash
  docker compose exec web python manage.py collectstatic
  ```
- Run custom scripts:  
  ```bash
  docker compose exec web python core/scraper.py
  ```

## Playwright

After building the Docker image, install Playwright browsers inside your container if needed:

```bash
docker compose exec web playwright install
```

## Migrations

Migrations should be committed to source control to keep schema changes in sync across environments.
