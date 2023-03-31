#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
  """
import urllib.request
import urllib.error
import sys

url = sys.argv[1]

try:
        with urllib.request.urlopen(url) as response:
                    print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
