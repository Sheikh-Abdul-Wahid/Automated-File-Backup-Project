# Automated File Backup Project

This Python project automates the process of backing up files from a source folder to a destination folder on a daily schedule.

## Features
- Automatically copies files from the source directory to the destination directory.
- Creates a backup folder with the current date as the folder name.
- Ensures no duplicate backups are created if the folder already exists.

## Technologies Used
- Python 3.12
- Libraries: `os`, `shutil`, `datetime`, `schedule`, `time`
