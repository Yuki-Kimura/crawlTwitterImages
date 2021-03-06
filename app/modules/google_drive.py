import io
import tempfile
import urllib
from pprint import pprint

import requests
from engine.config import config, show_path
from PIL import Image
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth(settings_file=show_path())
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)


def is_user_folder(screen_name):
    folder_list = drive.ListFile(
        {
            "q": "'{}' in parents\
               and trashed=false\
               and mimeType='application/vnd.google-apps.folder'".format(
                config["root_folder_id"]
            )
        }
    ).GetList()
    folders = dict()
    for folder in folder_list:
        folders.update({folder["title"]: folder["id"]})
    if screen_name in folders:
        return folders[screen_name]
    else:
        folder = drive.CreateFile(
            {
                "title": screen_name,
                "parents": [{"id": config["root_folder_id"]}],
                "mimeType": "application/vnd.google-apps.folder",
            }
        )
        folder.Upload()
        return folder["id"]


def is_image_folder(fid, fname):
    folder_list = drive.ListFile(
        {
            "q": "'{}' in parents\
               and trashed=false\
               and mimeType='application/vnd.google-apps.folder'".format(
                fid
            )
        }
    ).GetList()
    folders = dict()
    for folder in folder_list:
        folders.update({folder["title"]: folder["id"]})
    if fname in folders:
        return folders[fname]
    else:
        folder = drive.CreateFile(
            {
                "title": fname,
                "parents": [{"id": fid}],
                "mimeType": "application/vnd.google-apps.folder",
            }
        )
        folder.Upload()
        return folder["id"]


def save_images(images, folder_id):

    for image in images:
        save_folder = is_image_folder(folder_id, image["fname"])
        if image.get("is_video", 0):
            video_url = image["url"]
            mime = "video/mp4"

            tmpfile = tempfile.NamedTemporaryFile()
            urllib.request.urlretrieve(video_url, tmpfile.name)

            f = drive.CreateFile(
                {
                    "title": image["title"],
                    "mimeType": mime,
                    "parents": [{"kind": "drive#fileLink", "id": save_folder}],
                }
            )
            f.SetContentFile(tmpfile.name)
            f.Upload()
            f["description"] = image["description"]
            f.Upload()
            pprint(f)
            print("*" * 20)
            continue

        img = Image.open(io.BytesIO(requests.get(image["url"]).content))
        tmpfile = tempfile.TemporaryFile()
        img.save(tmpfile, img.format)
        mime = Image.MIME[img.format]
        f = drive.CreateFile(
            {
                "title": image["title"],
                "mimeType": mime,
                "parents": [{"kind": "drive#fileLink", "id": save_folder}],
            }
        )
        f.SetContentFile(tmpfile.name)
        f.Upload()
        f["description"] = image["description"]
        f.Upload()
        pprint(f)
        print("*" * 20)


if __name__ == "__main__":
    print(is_user_folder("test00"))

