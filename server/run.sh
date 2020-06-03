#!/bin/bash

docker run --name ntcontainer -p 3000:80 nettester 

echo "Container running at localhost:3000"
