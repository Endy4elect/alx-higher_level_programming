#!/bin/bash
# takes in a URL,send a GET request to the URL with curl, and display only body of a 200 status code response
curl -sL "$1"
