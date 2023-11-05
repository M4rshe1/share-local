import os

from flask import render_template
from .ext import EXT


def list_dir(share_root, path=""):
    parent = ""
    directory = []
    # if path != "":
        # directory.append({"type": "folder", "name": "..", "path": parent})

    for i in os.listdir(os.path.join(share_root, path)):
        # print(i + " " + str(os.path.isdir(os.path.join(share_root, path, i))))
        if os.path.isdir(os.path.join(share_root, path, i)):

            directory.append({"type": "folder", "name": i, "path": os.path.join(path, i)})
        else:
            ext = i.split(".")[-1]
            # print(ext)
            # print(EXT)
            for cat, extensions in EXT.items():
                # print(extensions)
                # print(cat)
                # print(extensions)
                if ext in extensions["extension"]:
                    directory.append({"type": "file", "name": i, "path": os.path.join(path, i), "ext": ext,
                                      "icon": extensions["icon"], "cat": cat.lower()})
                    break
            else:
                # unknown file type
                directory.append({"type": "file", "name": i, "path": os.path.join(path, i), "ext": ext,
                                  "icon": "fas fa-file", "cat": "unknown"})
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

    return render_template("index.html", files=directory, path=path, split=parents, parent=parent)
