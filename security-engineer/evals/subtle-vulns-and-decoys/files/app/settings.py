import yaml


def load_settings(path):
    with open(path) as f:
        return yaml.safe_load(f)
