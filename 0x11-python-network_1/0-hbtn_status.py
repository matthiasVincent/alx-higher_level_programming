#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import urllib.request


if __name__ == "__main__":
    data = {'User-Agent': 'Mozilla/6.0'}
    request = urllib.request.Request(
            "https://intranet.hbtn.io/status", headers=data)
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
