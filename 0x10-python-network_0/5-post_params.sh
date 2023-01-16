#!/bin/bash
# This script sends a POST request to a URL with parameters
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" -X POST "$1"
