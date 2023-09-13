@echo off
setlocal enabledelayedexpansion

rem Get the directory of the batch file
set "batch_dir=%~dp0"

rem Combine the batch file directory with .venv and activate the virtual environment
set "venv_dir=!batch_dir!.venv\Scripts\activate"
echo Activating virtual environment...
call "!venv_dir!"

rem Change to the project directory and start the Django development server
set "project_dir=!batch_dir!"
echo Starting Django development server in !project_dir!...
cd "!project_dir!"
python manage.py runserver
