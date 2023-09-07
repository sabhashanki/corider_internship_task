# corider_internship_task

### Abstract
The application should provide REST API endpoints for CRUD operations on a User resource.
The User resource should have the following fields:
* id (a unique identifier for the user)
* name (the name of the user)
*    email (the email address of the user)
*    password (the password of the user)

The application should connect to a MongoDB database.
The application should provide the following REST API endpoints:

*    GET /users - Returns a list of all users.
*    GET /users/<id> - Returns the user with the specified ID.
*    POST /users - Creates a new user with the specified data.
*    PUT /users/<id> - Updates the user with the specified ID with the new data.
*    DELETE /users/<id> - Deletes the user with the specified ID.

### Instruction

Load Docker tar.gz file

`docker load < busybox.tar.gz`

`sudo docker run -d -p 5000:5000 flask_mongo:4.0`

`sudo docker ps -a`    

Note down the container ID

`sudo docker exec -it <ContainerID> /bin/bash`

### Curl commands

READ ALL

`curl -X GET http://localhost:5000/users`

READ SPECIFIC

`curl -X GET http://localhost:5000/users/<user_id>`

DELETE

`curl -X DELETE http://localhost:5000/users/<user_id>`

CREATE

`curl -X POST --header "Content-Type: application/json" -d "{\"Name\":\"Shankesh\",\"Email\":\"abcd@gmail.com\",\"ID\":
95,\"Password\":\"efgrthyg\"}" http://localhost:5000/users`

UPDATE

`curl -X PUT --header "Content-Type: application/json" -d "{\"Name\":\"Preethi\",\"Email\":\"spreethi@gmail.com\",\"ID\":10,\"Password\":\"preetdfefi\"}" http://localhost:5000/users/10`

