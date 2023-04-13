import schedule
import time
import os

def job():
    print("Logging Performance Data \nInterrupt with Ctrl+C")
    while True:
        # Log the performance data
        os.system("docker stats --no-stream >> ./load_performance/stats.txt")

def stop_job():
    try:
        schedule.clear()
        exit(0)
    except:
        exit(1)

def main():
    schedule.every().day.at("21:00").do(job)
    schedule.every().day.at("22:00").do(stop_job)

    while True:
        schedule.run_pending()
        os.makedirs('./load_performance', exist_ok=True)
        # Print the remaining time until the next scheduled job
        print(f'Logger will run in {schedule.idle_seconds()} seconds', end='\r')
        time.sleep(1)

if __name__ == '__main__':
    main()