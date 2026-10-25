import os

UPLOAD_DIR = "/srv/uploads"


def read_upload(name):
    with open(os.path.join(UPLOAD_DIR, name), "rb") as f:
        return f.read()
