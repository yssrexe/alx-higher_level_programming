#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods
curl -siLX OPTIONS "$1" | grep Allow | cut -d ":" -f 2 | xargs
