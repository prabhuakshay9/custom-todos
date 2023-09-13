# TODOS

This is a custom built todo website powered by Django. This tool is built as per internal requirements
and is not designed to host multiple users.

## Steps to get it Working:

1. Copy `.env.dist` contents to `.env` and set a SECRET_KEY
2. Create a Virtual environment in the base_dir with the following command:
   `python -m venv .venv`
3. Activate the virtual environment using `.venv\Scripts\activate.bat`
4. Install all dependencies using `pip install -r requirements-prod.txt`
5. Create Database using `python manage.py migrate`
6. Create Superuser using `python manage.py createsuperuser`
7. Create a task to run the `start_server.bat` everytime the system starts
8. Create a task to run the `backup_db.bat` as required