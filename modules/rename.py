import os

from flask import redirect


def rename(share_root, path, form=None):
    new_name = form["new_name"]
    old_name = form["old_name"]
    parent_path = path.split(old_name)[0]

    if new_name != "":
        os.rename(os.path.join(share_root, parent_path, old_name), os.path.join(share_root, parent_path, new_name))

    return redirect(os.path.join(path.split(old_name)[0]))
