# Pacer Coding Challenge

## How to run locally

1. Install Docker

2. Create an environment file .env with variables below:

   ```sh
   DB_ENGINE=<value>
   DB_NAME=<value>
   DB_USER=<value>
   DB_PASSWORD=<value>
   DB_HOST=<value>
   DB_PORT=5432
   SECRET_KEY=<value>
   DEBUG=True # Set this to False for Prod environment
   USE_RDS=False # If set to False, app will use default db.sqlite3. Otherwise, it will use DB variables above
   ```

3. Run app via Docker Compose

   ```sh
   docker-compose up --build
   ```

4. On browser, go to localhost/api/healthcheck

5. Other URLs:
   - get_score API: /api/score/get_score?input=444
   - Admin panel: /admin_panel

## How to test

1. Install dependencies:

   - python3
   - pip3
   - virtualenv

2. Setup Python3 virtual environment

   ```sh
   cd pacer-app
   python3 -m virtualenv .venv
   source .venv/bin/activate
   ```

3. Install Python packages

   ```sh
   pip3 install -r requirements
   ```

4. Set SECRET_KEY, DEBUG and USE_RDS variables

5. Run unit tests:
   ```sh
   python3 manage.py test
   ```
