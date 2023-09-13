import os
import shutil
import time

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create a backup folder and take a SQLite database backup'

    def handle(self, *args, **options):
        # Define your base_dir where the backup folder should be created
        base_dir = settings.BASE_DIR
        backup_folder = os.path.join(base_dir, 'backup')

        # Check if the backup folder exists, and if not, create it
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)

        # Get the current date and time in the specified format
        current_date = time.strftime("%d_%m_%Y_%H_%M")

        # Create a folder inside the backup folder with the current date
        backup_folder_path = os.path.join(backup_folder, current_date)
        os.makedirs(backup_folder_path)

        # Define the name for the SQLite database backup file
        database_file = settings.DATABASES['default']['NAME']
        backup_file = os.path.join(backup_folder_path, 'db_backup.sqlite')

        # Copy the SQLite database file to the backup folder
        try:
            shutil.copy(database_file, backup_file)
            self.stdout.write(self.style.SUCCESS(f'Successfully created SQLite database backup: {backup_file}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to create SQLite database backup: {str(e)}'))
