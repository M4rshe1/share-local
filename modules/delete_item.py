import os
import shutil

from flask import redirect


def delete_item(share_root, path):
    parent_path = path.split("/")[:-1]
    parent_path = "/".join(parent_path)
    if parent_path == "":
        parent_path = "/"

    item_path = os.path.join(share_root, path).replace("\\", "/")
    print("Deleting: " + item_path)
    if os.path.exists(item_path):
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)
    else:
        raise Exception("The path does not exist")
    return redirect(os.path.join("/", parent_path))
