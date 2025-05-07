#!/bin/bash

echo "Getting token..."

# Get access token
RESPONSE=$(curl -s -X POST http://127.0.0.1:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"username": "admin_user", "password": "admin_user123"}')


# Check if RESPONSE is empty
if [ -z "$RESPONSE" ]; then
  echo "Failed to get token response. Check if the server is running."
  exit 1
fi

# Extract access token
TOKEN=$(echo "$RESPONSE" | jq -r .access)

# Check if token is non-empty
if [[ -z "$TOKEN" || "$TOKEN" == "null" ]]; then
  echo "Failed to get valid access token."
  exit 1
fi

# Create property
echo "Creating property with token..."
curl -s -X POST http://127.0.0.1:8000/api/properties/ \
-H "Authorization: Bearer $TOKEN" \
-H "Content-Type: application/json" \
-d '{
  "address": "2 test street",
  "postcode": "SW2T EST",
  "city": "Test Town Two",
  "num_rooms": 2
}' | jq .
