#!/usr/bin/python3
"""
Python module that makes a get request to given URL and displays
the request's unique ID
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('x-request-id'))
