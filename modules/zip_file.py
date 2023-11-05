import zipfile
import os


def zip_folder(folder_path):
    # Ensure that the output path ends with ".zip"
    output_path = folder_path + ".zip"

    # Create a new ZIP file
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through the folder and add its contents to the ZIP file
        for folder_name, folders, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(folder_name, filename)
                # Add the file to the ZIP archive using the relative path within the folder
                zipf.write(file_path, os.path.relpath(file_path, folder_path))