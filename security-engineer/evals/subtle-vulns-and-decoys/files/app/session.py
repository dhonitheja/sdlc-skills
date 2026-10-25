import base64
import hashlib
import hmac
import os
import pickle

SECRET = os.environ.get("SESSION_SECRET", "dev").encode()


def load_session(cookie):
    data = base64.b64decode(cookie)
    return pickle.loads(data)


def verify(sig, payload):
    expected = hmac.new(SECRET, payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, sig)
