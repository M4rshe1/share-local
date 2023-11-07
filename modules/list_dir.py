import datetime
import os

from flask import render_template
from .ext import EXT


def list_dir(share_root, path="", settings=None):
    parent = ""
    directory = []
    # if path != "":
        # directory.append({"type": "folder", "name": "..", "path": parent})

    dir_list = os.listdir(os.path.join(share_root, path))
    # sort directories first and then the file by their file extension
    dir_list.sort(key=lambda x: (os.path.isdir(os.path.join(share_root, path, x)), x.split(".")[-1]))
    # sort by filer type
    dir_list.sort(key=lambda f: not os.path.isdir(os.path.join(share_root, path, f)))

    for i in dir_list:
        created_at = os.path.getctime(os.path.join(share_root, path, i))
        last_modified = os.path.getmtime(os.path.join(share_root, path, i))
        size = os.path.getsize(os.path.join(share_root, path, i))

        # convert time to human readable format
        created_at = datetime.datetime.fromtimestamp(created_at).strftime('%Y-%m-%d %H:%M:%S')
        last_modified = datetime.datetime.fromtimestamp(last_modified).strftime('%Y-%m-%d %H:%M:%S')

        if os.path.isdir(os.path.join(share_root, path, i)):
            directory.append({"type": "folder", "name": i,
                              "path": os.path.join(path, i).replace('\\', '/'),
                              "created_at": created_at, "last_modified": last_modified, "size": size,
                              "icon": "fas fa-folder", "cat": "folder"})
        else:
            ext = i.split(".")[-1]
            # print(ext)
            # print(EXT)
            for cat, extensions in EXT.items():
                # print(extensions)
                # print(cat)
                # print(extensions)
                if ext in extensions["extension"]:
                    directory.append({"type": "file", "name": i,
                                      "path": os.path.join(path, i).replace('\\', '/'), "ext": ext,
                                      "icon": extensions["icon"], "cat": cat.lower(), "created_at": created_at,
                                      "last_modified": last_modified, "size": size})
                    break
            else:
                # unknown file type
                directory.append({"type": "file", "name": i,
                                  "path": os.path.join(path, i).replace('\\', '/'), "ext": ext,
                                  "icon": "fas fa-file", "cat": "unknown", "created_at": created_at,
                                  "last_modified": last_modified, "size": size})
            # for cat, extensions in EXT.items():
            #     if ext in extensions:
            #         directory.append({"type": "file", "name": i, "path": os.path.join(path, i), "ext": ext})
            #         break
            # else:
            #     # unknown file type
            #     directory.append({"type": "file", "name": i, "path": os.path.join(path, i), "ext": ext})
    # print(directory)
    tmp = path.split("/")
    parents = [{"name": "", "path": "/"}]
    for i in tmp:
        if i != "":
            parents.append({"name": i, "path": os.path.join(parents[-1]["path"], i)})
    # print(parents)
    split = path.split("/")
    if split[-1] == "":
        split.pop(-1)
    if len(split) > 0:
        # remove last element
        index = len(split) - 1
        split.pop(index)
        parent = "/".join(split)
    return render_template("index.html", files=directory, path=path, split=parents, parent=parent,
                           length=len(directory), settings=settings)
