#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import requests
import sys


if __name__ == "__main__":
    # r = requests.get("https://intranet.hbtn.io/status")
    r = request.get(sys.argv[1]
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
