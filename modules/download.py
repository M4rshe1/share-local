import os
import threading
from flask import send_from_directory, redirect
from modules import zip_folder, safe_remove_file


def download(share_root, path):
    download_path = os.path.join(share_root, path)
    if os.path.exists(download_path):
        if os.path.isdir(download_path):
            # generate zip file
            zip_folder(download_path)
            response = send_from_directory(share_root, path + ".zip", as_attachment=True)
            # Delete the file after it's sent for download
            # os.remove(os.path.join(share_root, path + ".zip"))
            delete_thread = threading.Thread(target=safe_remove_file,
                                             args=(os.path.join(share_root, path + ".zip"),))
            delete_thread.daemon = True
            delete_thread.start()
            return response
        else:
            return send_from_directory(share_root, path, as_attachment=True)
    return redirect("/")
