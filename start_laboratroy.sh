#!/bin/bash

cd server
vagrant up &

cd ../client
vagrant up &

cd ../tester
vagrant up &
