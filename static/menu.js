function download_file(url) {
//    open link with the post method

    let form = document.createElement('form');
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

function copy_name(name) {
    const textArea = document.createElement("textarea");
    textArea.value = name;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand("copy");
    document.body.removeChild(textArea);
}