#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept using curl.
curl -s -X OPTIONS -I "$1" | grep -i allow | cut -d' ' -f2-
