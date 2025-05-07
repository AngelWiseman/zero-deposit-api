#!/bin/bash

# Check if the property ID is passed as an argument
if [ -z "$1" ]; then
  echo "Please provide a property ID."
  exit 1
fi

PROPERTY_ID=$1

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

# Delete property  by ID
echo "Deleting property with ID $PROPERTY_ID..."
curl -s -X DELETE http://127.0.0.1:8000/api/properties/$PROPERTY_ID/ \
-H "Authorization: Bearer $TOKEN" \
-H "Content-Type: application/json" | jq .
