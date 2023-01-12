import schedule
import time

# Local Imports
from data_collector import collector
from data_processor import process
from utils import init_db

def status_update():
    print("[STATUS UPDATE] Task Scheduler still running...")

def scheduled_task():
    try:
        # Run data collector module
        collector.main()
        # Run trained ML model
        process.main()
    except:
        print("Preprocessesing failed see data logs for more details")

# Schedule every Monday to Friday at 6PM
schedule.every().monday.at("18:00").do(scheduled_task)
schedule.every().tuesday.at("18:00").do(scheduled_task)
schedule.every().wednesday.at("18:00").do(scheduled_task)
schedule.every().thursday.at("18:00").do(scheduled_task)
schedule.every().friday.at("18:00").do(scheduled_task)

# Update Status every 5 mins
schedule.every(5).minutes.do(status_update)

init_db.main()
while True:
    schedule.run_pending()
    time.sleep(1)