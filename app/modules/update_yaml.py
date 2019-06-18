from pprint import pprint

import yaml
from engine.config import config, show_path


def update_yaml(sn_ids):
    config["screen_names_and_last_id"] = sn_ids
    print("yaml updated")
    pprint(config)
    print("$" * 20)
    with open(show_path(), "w") as f:
        f.write(yaml.dump(config, default_flow_style=False))
