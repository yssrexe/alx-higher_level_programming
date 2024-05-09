#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods
curl -siLX OPTIONS "$1" | grep allow | cut -d ":" -f 2 | xargs
