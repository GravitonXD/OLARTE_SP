import datetime
import requests
import os

"""
    Stress Test 1

    Testers direcotry contains a set of tools that will be used to automate tests for the alamAPI.
    All test logs are recorded to ./test_logs/tester_name.csv
    Logs are saved as csv for easier results management.
"""

def run_test():
    # Initialize the date
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    # Initialize time start, show only time (including milliseconds) as datetime object
    time_start = datetime.datetime.now().strftime("%H:%M:%S.%f")

    # Initialized test counters
    success = 0
    fail = 0

    # Start the test
    for i in range(500):
        response = requests.get("http://localhost:8000/")
        if response.status_code != 200:
            fail += 1
        else:
            success += 1
        print(f"Test {i+1} completed :: {response.status_code}")
    
    # Get time end
    time_end = datetime.datetime.now().strftime("%H:%M:%S.%f")

    # Get the total time elapsed from time_start to time_end

    total_time = datetime.datetime.strptime(time_end, "%H:%M:%S.%f") - datetime.datetime.strptime(time_start, "%H:%M:%S.%f")

    # Save the test results to a csv file
    # Check if the file exists

    action = "w" if not os.path.exists("test_logs/stress_test1.csv") else "a"
    with open("./test_logs/stress_test1.csv", action) as f:
        if action == "w":
            # Write the header [run_number, run_date, time_start, time_end, total_time, success, fail]
            f.write("run_number,run_date,time_start,time_end,total_time,success,fail\n")
            # Write the results
            f.write(f"1,{date},{time_start},{time_end},{total_time},{success},{fail}\n")
        else:
            # Check the last run number
            with open("./test_logs/stress_test1.csv", "r") as c:
                last_run_number = len(c.readlines()) - 1
            # Write the results
            f.write(f"{last_run_number+1},{date},{time_start},{time_end},{total_time},{success},{fail}\n")
            c.close()
    f.close()
    

if __name__ == '__main__':
    run_test()