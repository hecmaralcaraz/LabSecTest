#!/bin/bash

cd server
vagrant halt &

cd ../client
vagrant halt &

cd ../tester
vagrant halt &
