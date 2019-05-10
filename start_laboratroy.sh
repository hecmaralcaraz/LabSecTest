#!/bin/bash

cd server
vagrant up 1> .log_start.log &

cd ../client
vagrant up 1> .log_start.log &
vagrant reload 1> .log_start.log &

cd ../tester
vagrant up 1> .log_start.log &
vagrant reload 1> .log_start.log &
echo "ok"
