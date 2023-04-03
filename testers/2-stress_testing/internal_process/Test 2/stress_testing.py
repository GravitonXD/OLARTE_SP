import os
import time
import schedule

def task():
    # Run 'manual_run.py' 100 times
    for i in range(100):
        start_time = time.time()
        print(f"Running process.py for the {i+1} time")
        try:
            os.system('python3 /preprocessor/data_processor/process.py')
            end_time = time.time()
            # Store the results in a file
            with open("/data/db/stress_test_results/results.csv", "a") as f:
                # Run Number, Start Time, End Time, Total Time, Status (1  - Success)
                f.write(f"{i+1},{start_time},{end_time},{end_time-start_time},{1}\n")
        except Exception as e:
            end_time = time.time()
            # Store the results in a file
            with open("/data/db/stress_test_results/results.csv", "a") as f:
                # Run Number, Start Time, End Time, Total Time, Status (0 - Failure)
                f.write(f"{i+1},{start_time},{end_time},{end_time-start_time},{0}\n")


def main():
    # Create a directory to store the results
    os.makedirs("/data/db/stress_test_results", exist_ok=True)

    # Run a task every 11:15 PM
    schedule.every().day.at("17:38").do(task)

    while True:
        # Print the remaining time until the next scheduled job
        print(f'Next task will run in {schedule.idle_seconds()} seconds', end='\r')
        # Run pending tasks
        schedule.run_pending()
        time.sleep(1)
    
    

if __name__ == '__main__':
    main()