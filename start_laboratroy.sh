#!/bin/bash

cd server
time vagrant up >> ../.log_start.log

cd ../client
time vagrant up >> ../.log_start.log
time vagrant reload >> ../.log_start.log

cd ../tester
time vagrant up >> ../.log_start.log
time vagrant >> ../.log_start.log
clear
echo "ok"
