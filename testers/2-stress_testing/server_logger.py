import schedule
import time
import os

def job():
    print("Logging Performance Data \nInterrupt with Ctrl+C")
    while True:
        # Log the performance data
        os.system("docker stats --no-stream >> ./server_performance_stress/stats.txt")

def main():
    schedule.every().day.at("23:15").do(job)

    while True:
        schedule.run_pending()
        os.makedirs('./server_performance_stress', exist_ok=True)
        # Print the remaining time until the next scheduled job
        print(f'Logger will run in {schedule.idle_seconds()} seconds', end='\r')
        time.sleep(1)

if __name__ == '__main__':
    main()