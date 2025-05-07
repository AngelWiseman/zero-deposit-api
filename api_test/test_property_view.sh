#!/bin/bash

#!/bin/bash

# Check if the property ID is passed as an argument
if [ -z "$1" ]; then
  echo "No property ID provided. Viewing all properties..."
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

# Build the request URL
if [ -z "$PROPERTY_ID" ]; then
  echo "No property ID provided. Viewing all properties..."
  URL="http://127.0.0.1:8000/api/properties/"
else
  echo "Viewing property with ID $PROPERTY_ID..."
  URL="http://127.0.0.1:8000/api/properties/$PROPERTY_ID/"
fi

# Make the GET request
curl -s -X GET "$URL" \
-H "Authorization: Bearer $TOKEN" \
-H "Content-Type: application/json" | jq -c . | jq .
