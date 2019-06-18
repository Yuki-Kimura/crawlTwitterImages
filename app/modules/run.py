from pprint import pprint

from .twitter_api import search_image
from .google_drive import is_user_folder, save_images
from engine.config import config
from .update_yaml import update_yaml

def run():
    try:
        ids = config['screen_names_and_last_id']
        pprint(ids)
        sn_ids = dict()
        for screen_name, post_id in ids.items():
            folder_id = is_user_folder(screen_name)
            new_id, images = search_image(screen_name, post_id)
            sn_ids.update({screen_name: new_id})
            save_images(images, folder_id)
        update_yaml(sn_ids)
    except Exception as e:
        print('-------------------------')
        print('ERROR:')
        print(e)
        print('-------------------------')

if __name__ == "__main__":
    run()
