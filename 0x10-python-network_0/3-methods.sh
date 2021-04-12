#!/bin/bash
# takes in a URL and displays all HTTP methods the applicable
curl -sI "$1" | grep Allow | cut -d " " -f2-
