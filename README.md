# Django

# Inorder to create a token for a user run 

curl -X Post -H "Content-Type: application/json" -d "{\"username\":\"your_username\", \"password\":\"your_password\"}" http://localhost:8000/api-token-auth/


# Check your auth key 

curl -v -H 'Authorization: Token InsertYourAuthKeyHere' http://localhost:8000/api/notes
