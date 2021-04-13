#!/usr/bin/python3
"""
Takes in a URL, sends request to that URL and displays
value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as reponse:
    for header in reponse.getheaders():
        if header[0] == 'X-Request-Id':
            print(header[1])
