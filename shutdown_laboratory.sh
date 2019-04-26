#!/bin/bash

cd server
vagrant halt 1> .log_shutdown.log &

cd ../client
vagrant halt 1> .log_shutdown.log &

cd ../tester
vagrant halt 1> .log_shutdown.log &
