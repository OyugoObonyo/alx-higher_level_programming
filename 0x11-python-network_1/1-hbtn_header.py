#!/usr/bin/python3
"""
Takes in a URL, sends request to that URL and displays
value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        requestId = response.getheader("X-Request-Id")
        print(requestId)
