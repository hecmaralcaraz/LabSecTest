#!/bin/bash

cd server
vagrant up >> ../.log_start.log

cd ../client
vagrant up >> ../.log_start.log
vagrant reload >> ../.log_start.log

cd ../tester
vagrant up >> ../.log_start.log
vagrant reload >> ../.log_start.log
clear
echo "Please go to directory tester and execute vagrant ssh"
echo "Example:"
echo "$ cd tester"
echo "$ vagrant ssh"
