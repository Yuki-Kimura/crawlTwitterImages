from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import requests
from PIL import Image
import io
import tempfile
import mimetypes
from engine.config import config, show_path


gauth = GoogleAuth(settings_file=show_path())
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

# image_url = 'https://1.bp.blogspot.com/-TEfo3GegD2s/XKGJu6JrLzI/AAAAAAABSHs/_loS9jFH9GkNq7CDvHuKthAnoTy4VTWAACLcBGAs/s800/gengou_happyou_reiwa_kakageru.png'
image_url = 'https://pbs.twimg.com/media/D5nfVOiU0AAUkHA.jpg:large'

image = Image.open(io.BytesIO(requests.get(image_url).content))


folder_id = '1DLgK_ZkwBjTh9YKhXgEgPtmMqUQ2JVQB'
tmpfile = tempfile.TemporaryFile()
image.save(tmpfile, image.format)
print(image.format)
print(tmpfile.name)
mime = Image.MIME[image.format]
print(mime)
print(config['twitter'])
file_title = 'testp.' + image.format.lower()
f = drive.CreateFile({
    'title': file_title,
    'mimeType': mime,
    'parents': [{'kind': 'drive#fileLink', 'id': folder_id}]
    })
f.SetContentFile(tmpfile.name)
f.Upload()
f['description'] = 'For mime test. This is ReiwaOjisan'
f.Upload()
