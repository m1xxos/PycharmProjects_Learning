import requests


def get_content_type(url):
    r = requests.get(url)
    return r.headers["Content-Type"]


# `print(get_content_type("http://github.com"))
