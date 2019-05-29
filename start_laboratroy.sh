#!/bin/bash

cd server
vagrant up >> ../.log_start.log

cd ../client
vagrant up >> ../.log_start.log

cd ../tester
vagrant up >> ../.log_start.log
clear
echo "ok"
