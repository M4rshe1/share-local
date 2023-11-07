function show_prop(prop = {}) {
    // check for an existing dialog
    let check_dialog = document.getElementById('prop_dialog');
    if (check_dialog) {
        document.body.removeChild(check_dialog);
    }


    console.log(prop)
    // {"type": "file", "name": i, "path": os.path.join(path, i), "ext": ext,
    //     "icon": "fas fa-file", "cat": "unknown", "created_at": created_at, "last_modified": last_modified, "size": size}
    let name = prop.name;
    let type = prop.type;
    let ext = prop.ext;
    let icon = prop.icon;
    let cat = prop.cat;
    let path = prop.path;
    let size = prop.size;
    let date = prop.last_modified;
    let created = prop.created_at;
//     create a dialog that shows the properties of the file
    let dialog = document.createElement('div');
    dialog.id = 'prop_dialog';
    dialog.className = 'dialog';
    let close_btn_div = document.createElement('div');
    close_btn_div.className = 'close_btn_div prop_div';

    let close_btn = document.createElement('button');
    close_btn.className = 'close_btn';
    close_btn.innerHTML = 'X';
    close_btn.onclick = function () {
        document.body.removeChild(dialog);
    };
    let title = document.createElement('span');
    title.className = 'dialog_title';
    title.innerHTML = 'Properties';
    close_btn_div.appendChild(title);
    close_btn_div.appendChild(close_btn);

    let name_div = document.createElement('div');
    name_div.className = 'prop_div';
    name_div.innerHTML = name;
    let type_div = document.createElement('div');
    type_div.className = 'prop_div';
    // type_div.innerHTML = 'Filetype      : ' + type;
    type_div.innerHTML = '<span class="prop_name">Filetype</span>' + ": " + type + ' (' + ext + ')';
    let size_div = document.createElement('div');
    size_div.className = 'prop_div';
    // size_div.innerHTML = 'Size          : ' + size / 1000000 + ' MB' + ' (' + size + ' bytes)';

    let new_size = 0;
    if (size < 1000) {
        new_size = size + ' bytes';
    } else if (size < 1000000) {
        new_size = Math.round(size / 1000) + ' KB' +" (" + size + ' bytes)';
    } else if (size < 1000000000) {
        new_size = Math.round(size / 1000000) + ' MB' +" (" + size + ' bytes)';
    } else {
        new_size = Math.round(size / 1000000000) + ' GB' +" (" + size + ' bytes)';
    }
    size_div.innerHTML = '<span class="prop_name">Size</span>' + ": " + new_size;
    let date_div = document.createElement('div');
    date_div.className = 'prop_div';
    date_div.innerHTML = '<span class="prop_name">Modified</span>' + ": " + date;
    let created_div = document.createElement('div');
    created_div.className = 'prop_div';
    created_div.innerHTML = '<span class="prop_name">Created</span>' + ": " + created;
    let cat_div = document.createElement('div');
    cat_div.className = 'prop_div';
    // cat_div.innerHTML = 'Category       : ' + cat;
    cat_div.innerHTML = '<span class="prop_name">Category</span>' + ": " + cat;
    let path_div = document.createElement('div');
    path_div.className = 'prop_div';
    // path_div.innerHTML = 'Path: /' + path;
    path_div.innerHTML = '<span class="prop_name">Path</span>' + ": /" + path.replace(/\\/g, '/');
    let icon_div = document.createElement('div');
    icon_div.className = 'prop_div';
    let icon_i = document.createElement('i');
    icon_i.className = icon + ' fa-2x ' + 'ext-' + cat;
    icon_div.appendChild(icon_i);
    dialog.appendChild(close_btn_div);


    let section1 = document.createElement('div');
    let section2 = document.createElement('div');
    let section3 = document.createElement('div');
    let section4 = document.createElement('div');
    section1.className = 'section section1';
    section2.className = 'section section2';
    section3.className = 'section section3';
    section4.className = 'section section4';

    section1.appendChild(icon_div);
    section1.appendChild(name_div);
    if (type === 'file') {
        section2.append(type_div);
    }
    section2.append(cat_div);
    section3.append(path_div);
    section3.append(size_div);
    section4.append(date_div);
    section4.append(created_div);

    dialog.appendChild(section1);
    dialog.appendChild(section2);
    dialog.appendChild(section3);
    dialog.appendChild(section4);
    document.body.appendChild(dialog);

    // let isDragging = false;
    // let offsetX, offsetY;
    //
    // const dragElement = document.getElementById("prop_dialog");
    //
    // dragElement.addEventListener("mousedown", (e) => {
    //     isDragging = true;
    //     offsetX = e.clientX - dragElement.getBoundingClientRect().left;
    //     offsetY = e.clientY - dragElement.getBoundingClientRect().top;
    //     dragElement.style.cursor = "grabbing"; /* Change cursor style when dragging */
    // });
    //
    // document.addEventListener("mousemove", (e) => {
    //     if (!isDragging) return;
    //
    //     const x = e.clientX - offsetX;
    //     const y = e.clientY - offsetY;
    //
    //     dragElement.style.left = x + "px";
    //     dragElement.style.top = y + "px";
    // });
    //
    // document.addEventListener("mouseup", () => {
    //     isDragging = false;
    //     dragElement.style.cursor = "grab"; /* Restore cursor style */
    // });
}