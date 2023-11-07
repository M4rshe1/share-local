import os
from flask import redirect


def create_folder(share_root, path, form=None):
    folder_name = form["folder_name"]
    if folder_name != "":
        if not os.path.exists(os.path.join(share_root, path, folder_name)):
            os.mkdir(os.path.join(share_root, path, folder_name))
    return redirect(os.path.join("/", path, folder_name))

