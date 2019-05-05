from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from engine.config import config, show_path

gauth = GoogleAuth(settings_file=show_path())
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

file = drive.CreateFile({'title' : 'TwitterImageCrawl',
            'mimeType': 'application/vnd.google-apps.folder'})
file.Upload()

