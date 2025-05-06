#!/bin/bash

# Get the token by sending a POST request to the token endpoint
RESPONSE=$(curl -s -X POST http://127.0.0.1:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{
    "username": "admin123",
    "password": "admin123"
}')

# Print the raw response to check for errors
echo "Raw response: $RESPONSE"

# Extract the access token from the response using jq
export TOKEN=$(echo "$RESPONSE" | jq . '.access')
export REFRESH_TOKEN=$(echo "$RESPONSE" | jq . '.refresh')

# Print the token (optional)
echo "Access token: $TOKEN"
