# share-local
share-local is a simple file sharing tool for your local network. It is written in python and uses the flask framework.
With this tool you can share files and directories with your friends and colleagues in your local network.
For safety reasons, the tool dose also have a mode where you can create users with passwords and set rights for them.

## Supported file extensions
**EXEC** : exe, msi, bin, crx, com, appimage, run, apk, deb, rpm, jar,   
**FONT** : eot, otf, ttf, woff, woff2, pf2,   
**IMG** : 3dm, 3ds, max, bmp, dds, gif, jpg, jpeg, png, psd, xcf, tga, thm, tif, tiff, ai, eps, ps, svg, dwg, dxf, gpx, kml, kmz, webp, ico, jfif, jpe, stl, pdn,   
**ISO** : iso, img, vcd, dmg, toast, vdi, vmdk, vhd, hdd, hds, tc, truecrypt,   
**TORRENT** : torrent,   
**DATABASE** : db, dbf, mdb, pdb,   
**CONFIG** : ini, cfg, conf, config, properties, prop, settings, infreg,   
**DIAGRAMS** : drawio, dtmp, nsd, fprg,   
**VIDEO** : mp4, mkv, webm, avi, mov, wmv, mpg, mpeg, m4v, flv, swf, vob, mng, qt, mpv, m2v, m4p, m4v, ogv, ogm, ogx, rm, rmvb, asf, 3gp, 3g2, f4v, f4p, f4a, f4b,   
**AUDIO** : aac, aa, aac, dvf, m4a, m4b, m4p, mp3, msv, ogg, oga, raw, vox, wav, wma,   
**PDF** : pdf,   
**TEXT** : txt, in, out,   
**WORD** : doc, docx, odt, rtf, tex, wks, wps, wpd,   
**SHEET** : ods, xlr, csv,   
**EXCEL** : xls, xlsx, xlt, xlsm,   
**POWERPOINT** : ppt, pptx, odp, pps, ppsx,   
**ARCHIVE** : 7z, arj, deb, pkg, rar, rpm, tar.gz, z, zip, gz, xz, bz2, tar, tgz,   
**CODE** : ps1, c, cpp, py, java, class, cs, h, sh, swift, vb, js, css, scss, html, htm, php, asp, aspx, jsp, json, yaml, yml, xml, sql, md, pyc, pyo, dockerfile, gitignore, git, lua, rb, r, pl, go, ts, tsx, jsx, kt, kts, htmx, dart, perl, toml, sh, bash, zsh, fish, ps1, bat, cmd, vbs, vba, vbe, wsf, wsc, zig, graphql, cbl, cob, pascal, f, f90, for, lisp, elixir, elm, erlang, hs, lhs, jl, svelte,

## Features
 - Share a directory as website
 - Share a file as website
 - Copy files
 - Move files
 - Delete files
 - Rename files
 - Create new directory
 - Upload files
 - Download files
 - Create new file
 - zip folder
 - custom users
 - custom password
 - user rights
 - file colors

![features.png](static%2Ffeatures.png)

## Installation
### Windows
 - Clone the repository
 - Install python if you don't have it already
 - Install the requirements with `pip install -r requirements.txt`
 - Run the server with `python app.py`
 - select the directory you want to share
 - open the link in your browser
 - enjoy!!!

### Set password an user rights
 - open the file `config.json`
 - set the value of `password` to your password
 -  Be sure to enable the ``LOGIN_REQUIRED_OVERRIDE`` to ``True`` at the top of the ``app.py`` file
 - Set the user rights  
#### Example:
````
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
````