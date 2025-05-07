#!/bin/bash

curl -s -X POST http://127.0.0.1:8000/api/users/register/ \
-H "Content-Type: application/json" \
-d '{
"username": "admin_user",
    "email": "admin_user@example.com",
    "password": "admin_user123",
    "role": "admin"
}' | jq . 
