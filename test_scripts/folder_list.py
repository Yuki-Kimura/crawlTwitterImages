from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from pprint import pprint

from engine.config import config, show_path


gauth = GoogleAuth(settings_file=show_path())
gauth.CommandLineAuth()
drive = GoogleDrive(gauth) # Create GoogleDrive instance with authenticated GoogleAuth instance

file_list = drive.ListFile({'q': "'1FFYzUMMF-0Ku-wX26SCIPM8TTRbLxlT5' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s, MIME: %s' % (file1['title'], file1['id'], file1['mimeType']))

