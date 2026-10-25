import os


def auth_header():
    return {"Authorization": "Bearer " + os.environ["API_TOKEN"]}
