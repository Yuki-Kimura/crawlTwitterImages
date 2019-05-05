import yaml
from os import path

with open(path.join(path.dirname(__file__), "config.yml")) as f:
    config = yaml.load(f)

def show_path():
    return path.join(path.dirname(__file__), "config.yml")

