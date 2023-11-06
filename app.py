import threading
import flask
from flask import request, send_from_directory, redirect, Response
from modules import *
import os

app = flask.Flask(__name__)

share_root = "C:/Users/Colin/Downloads/SORTED"
if not os.path.exists(share_root):
    share_root = select_folder()


# from flask_httpauth import HTTPBasicAuth
# from werkzeug.security import check_password_hash, generate_password_hash
#
# auth = HTTPBasicAuth()
# user = 'admin'
# pw = '1234'
# users = {
#     user: generate_password_hash(pw)
# }
#
#
# @auth.verify_password
# def verify_password(username, password):
#     # Verify the provided username and password
#     if username in users:
#         return check_password_hash(users.get(username), password)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
# @auth.login_required
def index(path=None):
    # get the form data$
    form = request.form.to_dict()
    print(form)

    if form != {} and "action" in form and form["action"] == "download":
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
    else:
        # print("Accessing: /" + path)
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


if __name__ == '__main__':
    print("The Webserver is sharing the folder: " + share_root + " on port 8888")
    os.chdir(share_root)
    app.run(debug=True, host='0.0.0.0', port=8888)
