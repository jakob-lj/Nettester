#!/bin/bash
sudo ./build.sh
sudo docker run --name ntdepcontainer -d -p 5522:80 nettester
