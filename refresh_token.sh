#!/bin/bash

# Make sure REFRESH_TOKEN is set
if [ -z "$REFRESH_TOKEN" ]; then
  echo "Error: REFRESH_TOKEN is not set. Run get_token.sh first."
  exit 1
fi

# Send request to refresh the token
RESPONSE=$(curl -s -X POST http://127.0.0.1:8000/api/token/refresh/ \
-H "Content-Type: application/json" \
-d '{
  "refresh": "'"$REFRESH_TOKEN"'"
}')

echo "Raw response: $RESPONSE"

# Extract the new access token
NEW_TOKEN=$(echo "$RESPONSE" | jq . '.access')

# Check if the token was refreshed
if [ "$NEW_TOKEN" == "null" ]; then
  echo "Failed to refresh token."
else
  export TOKEN=$NEW_TOKEN
  echo "Refreshed access token: $TOKEN"
fi
