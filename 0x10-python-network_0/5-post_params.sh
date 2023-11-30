#!/bin/bash
# Bash scripts that sends a POST request to a given URL.
curl -s -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
