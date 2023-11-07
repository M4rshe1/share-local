import os

from flask import redirect


def upload(share_root, path, request):
    # print all file names
    for f in request.files.getlist('file'):
        print(f.filename)
        f.save(os.path.join(share_root, path, f.filename))
    return redirect(os.path.join("/", path))
