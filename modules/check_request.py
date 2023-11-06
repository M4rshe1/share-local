import os
from flask import Response, send_from_directory, redirect
from modules import list_dir


def check_request(share_root, request, path):
    if os.path.exists(os.path.join(share_root, request.path[1:])):
        if os.path.isdir(os.path.join(share_root, request.path[1:])):
            # getting parent directory
            return list_dir(share_root, path)
        else:
            if os.path.exists(os.path.join(share_root, request.path[1:])):
                try:
                    with open(os.path.join(share_root, request.path[1:]), "r") as file:
                        content = file.read()
                    return Response(content, mimetype='text/plain')
                except UnicodeDecodeError:
                    return send_from_directory(share_root, request.path[1:])
    return redirect("/")
