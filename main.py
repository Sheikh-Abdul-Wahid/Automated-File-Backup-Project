import os
import datetime
import time
import schedule
import shutil

source_directory = "C:\\Path\\To\\Source"            # Update the source directory with your desired paths
destination_directory = "C:\\Path\\To\\Destination"  # Update the destination directory with your desired paths

def copy_folder_to_directory(source, destination):
    today = datetime.date.today()
    print(today)
    new_destination_directory = os.path.join(destination, str(today))
    
    try:
        shutil.copytree(source, new_destination_directory)
        print(f"Folder copied to: {new_destination_directory}")
    except FileExistsError:
        print(f"Folder already exists in: {destination}")

""" 
Define a separate function like run() and place the function call inside it:
def run():
        copy_folder_to_directory(source_directory, destination_directory)

schedule.every().day.at("16:36").do(run)
"""

schedule.every().day.at("18:21").do(lambda: copy_folder_to_directory(source_directory, destination_directory))

while True:
    schedule.run_pending()
    time.sleep(60)
