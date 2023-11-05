import os
import time


def safe_remove_file(file_path):
    max_retries = 10  # Adjust this as needed
    retries = 0
    time.sleep(10)

    while retries < max_retries:
        time.sleep(1)
        try:
            os.remove(file_path)
            break  # File successfully deleted, exit the loop
        except PermissionError:
            time.sleep(1)  # Wait for 1 second and then retry
            retries += 1
    else:
        print(f"Failed to delete {file_path} after {max_retries} retries")