#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode()
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode("utf-8")
        print(body)
