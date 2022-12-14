# About this directory 
Testers direcotry contains a set of tools that will be used to automate tests for the alamAPI.

All test logs are recorded to ./test_logs/tester_name.csv
Logs are saved as csv for easier results management.

# RUN docker build
1. cd to src
2. docker-compose build (skip if already done)
3. docker-compose up

# Testers
1. stress_test1.py :: This test will run a total of 100,000 requests to the api(home).