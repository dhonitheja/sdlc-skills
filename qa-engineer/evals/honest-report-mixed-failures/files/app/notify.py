import acme_notify_sdk


def send(message):
    return acme_notify_sdk.Client().send(message)
