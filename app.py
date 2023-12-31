# Author: M4rshe1
# Description: This is a script that will share a folder on the local network as a website.
# It will allow users to download files, upload files and delete files.
# It will also allow users to navigate through the folder structure.

# ------------------------------------------------------------ #
#                           Imports                            #
# ------------------------------------------------------------ #

import flask
from flask import request, redirect, render_template
from modules import *
import os
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash

app = flask.Flask(__name__)

# ------------------------------------------------------------ #
#                           Settings                           #
# ------------------------------------------------------------ #

# If it is empty, the user will be prompted to select a folder
SHARE_ROOT_OVERRIDE = "C:/Users/Colin/Downloads/SORTED"

# Login override will override all other settings.
# So that only logged-in, with the correct respective permissions, can access the website.
# TODO: Implement Move and copy
LOGIN_REQUIRED_OVERRIDE = True
UPLOAD_ENABLED_OVERRIDE = False
DELETE_ENABLED_OVERRIDE = False
RENAME_ENABLED_OVERRIDE = False
CREATE_FOLDER_ENABLED_OVERRIDE = False
DOWNLOAD_ENABLED_OVERRIDE = True
OPEN_BROWSER = False
share_root = ""

# ------------------------------------------------------------ #
#                           Helpers                            #
# ------------------------------------------------------------ #


if not os.path.exists(share_root) and SHARE_ROOT_OVERRIDE == "":
    share_root = select_folder()
    if os.path.exists(share_root) and OPEN_BROWSER:
        open_browser()
    else:
        raise Exception("The share root does not exist")
elif SHARE_ROOT_OVERRIDE != "" and os.path.exists(SHARE_ROOT_OVERRIDE):
    share_root = SHARE_ROOT_OVERRIDE
    if OPEN_BROWSER:
        open_browser()
else:
    raise Exception("The share root does not exist")

# ------------------------------------------------------------ #
#                           Auth                               #
# ------------------------------------------------------------ #

auth = HTTPBasicAuth()
users = {
    'admin': {
        'password': generate_password_hash('Bananen.123'),
        'enabled': True,
        'upload': True,
        'delete': True,
        'download': True,
        'rename': True,
        'create_folder': True
    },
    'guest': {
        'password': generate_password_hash('Bananen.123'),
        'enabled': True,
        'upload': False,
        'delete': False,
        'download': True,
        'rename': False,
        'create_folder': False
    }
}


@auth.verify_password
def verify_password(username, password):
    # Verify the provided username and password
    # print(username, password)
    if username in users:
        pw = users.get(username).get('password')
        return check_password_hash(pw, password)
    return False


# ------------------------------------------------------------ #
#                           Routes                             #
# ------------------------------------------------------------ #
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def navigate(path=None):
    form = request.form.to_dict()
    action = "show"
    if form != {} and "action" in form:
        action = form["action"]
    if LOGIN_REQUIRED_OVERRIDE:
        @auth.login_required
        def protected_path():
            user = users.get(auth.username())
            print("User: " + auth.username() + " is accessing: /" + path + " with action: " + action)
            if action == "download" and users.get(auth.username()).get('upload'):
                return download(share_root, path)
            elif action == "delete" and users.get(auth.username()).get('delete'): 
                # return safe_remove_file(os.path.join(share_root, path))
                return delete_item(share_root, path)
            elif action == "upload" and users.get(auth.username()).get('upload'):
                return upload(share_root, path, request)
            elif action == "rename" and users.get(auth.username()).get('rename'):
                return rename(share_root, path, form)
            elif action == "create_folder" and users.get(auth.username()).get('create_folder'):
                return create_folder(share_root, path, form)
            else:
                # print("Accessing: /" + path)
                return check_request(share_root, request, path, users.get(auth.username()))

        return protected_path()
    else:
        print("Accessing: /" + path + " with action: " + action)
        if action == "download" and DOWNLOAD_ENABLED_OVERRIDE:
            return download(share_root, path)
        elif action == "delete" and DELETE_ENABLED_OVERRIDE:
            return delete_item(os.path.join(share_root, path))
        elif action == "upload" and UPLOAD_ENABLED_OVERRIDE:
            return upload(share_root, path, request.files)
        elif action == "rename" and RENAME_ENABLED_OVERRIDE:
            return rename(share_root, path, form)
        elif action == "create_folder" and CREATE_FOLDER_ENABLED_OVERRIDE:
            return create_folder(share_root, path, form)
        else:
            # print("Accessing: /" + path)
            return check_request(share_root, request, path, {
                "enabled": True,
                "upload": UPLOAD_ENABLED_OVERRIDE,
                "delete": DOWNLOAD_ENABLED_OVERRIDE,
                "download": DOWNLOAD_ENABLED_OVERRIDE,
                "rename": RENAME_ENABLED_OVERRIDE
            })


# ------------------------------------------------------------ #
#                       Error Handlers                         #
# ------------------------------------------------------------ #
@app.errorhandler(404)
def page_not_found(e):
    return redirect("/")


if __name__ == '__main__':
    # share_root = select_folder()
    print("The Webserver is sharing the folder: " + share_root + " on port 8888. Login is required: "
          + str(LOGIN_REQUIRED_OVERRIDE))
    os.chdir(share_root)
    app.run(host='0.0.0.0', port=8888, debug=True)
