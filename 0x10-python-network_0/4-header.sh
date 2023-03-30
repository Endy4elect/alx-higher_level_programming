#!/bin/bash
# sends a GET request to the URL, and displays the body of the response sending header variable X-School-User-Id with the value 98 using curl
curl -s -H "X-School-User-Id: 98" "$1"
