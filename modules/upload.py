import os

from flask import redirect


def upload(share_root, path, request):
    # print all file names
    print(f"Uploading ({request.files.getlist('file')[0].filename}) to: " + os.path.join(share_root, path))
    for f in request.files.getlist('file'):
        print(f.filename)
        f.save(os.path.join(share_root, path, f.filename))
    return redirect(os.path.join("/", path))
