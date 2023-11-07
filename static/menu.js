function download_file(url) {
    let form = document.createElement('form');
    let input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'action';
    input.value = 'download';
    form.appendChild(input);
    form.action = url;
    form.method = 'POST';
    document.body.appendChild(form);
    form.submit();
    document.body.removeChild(form);
}


function open_new_tab(url) {
    window.open(url, '_blank');
}

function copy_link(url) {
    const textArea = document.createElement("textarea");
    let base_url = window.location.protocol + "//" + window.location.host;
    textArea.value = base_url + "/" + url;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand("copy");
    document.body.removeChild(textArea);
}

// function copy_name(name) {
//     const textArea = document.createElement("textarea");
//     textArea.value = name;
//     document.body.appendChild(textArea);
//     textArea.select();
//     document.execCommand("copy");
//     document.body.removeChild(textArea);
// }

function upload_folder(url) {
    // open folder selection window
    let input = document.createElement('input');
    input.type = 'file';
    input.multiple = true;
    input.webkitdirectory = true;
    input.directory = true;
    input.click();
    input.onchange = function () {
        let form = document.createElement('form');
        let input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'action';
        input.value = 'upload';
        form.appendChild(input);
        form.action = url;
        form.method = 'POST';
        document.body.appendChild(form);
        form.submit();
        document.body.removeChild(form);
    };


}

function upload_file(url) {
    // open file selection window
    let input = document.createElement('input');
    input.type = 'file';
    input.multiple = true;
    input.click();
    input.onchange = function () {
        let form = document.createElement('form');
        let input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'action';
        input.value = 'upload';
        form.appendChild(input);
        form.action = url;
        form.method = 'POST';
        document.body.appendChild(form);
        form.submit();
        document.body.removeChild(form);
    };
}

function create_folder(url) {
    let folder_name = prompt("Please enter folder name", "New Folder");
    if (folder_name != null) {
        let form = document.createElement('form');
        let input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'action';
        input.value = 'create_folder';
        form.appendChild(input);
        input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'folder_name';
        input.value = folder_name;
        form.appendChild(input);
        form.action = url;
        form.method = 'POST';
        document.body.appendChild(form);
        form.submit();
        document.body.removeChild(form);
    }
}

function rename_file(url, file_name) {
    let new_name = prompt("Please enter folder name", file_name);
    console.log("rename: " + url);
    if (new_name != null) {
        let form = document.createElement('form');
        let input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'action';
        input.value = 'rename';
        form.appendChild(input);
        input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'new_name';
        input.value = new_name;
        form.appendChild(input);
        input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'old_name';
        input.value = file_name;
        form.appendChild(input);
        form.action = url;
        form.method = 'POST';
        document.body.appendChild(form);
        form.submit();
        document.body.removeChild(form);
    }

}

function delete_file(url) {
    console.log("delete: " + url);
    let form = document.createElement('form');
    let input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'action';
    input.value = 'delete';
    form.appendChild(input);
    form.action = url;
    form.method = 'POST';
    document.body.appendChild(form);
    form.submit();
    document.body.removeChild(form);
}