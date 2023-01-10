import schedule
import time

# Local Imports
from data_collector import collector
from data_processor import process

def scheduled_task():
    try:
        # Run data collector module
        collector.main()
        # Run trained ML model
        process.main()
    except:
        Exception("Preprocessesing failed see data logs for more details")

# Schedule every Monday to Friday at 6PM
schedule.every().monday.at("18:00").do(scheduled_task)
schedule.every().tuesday.at("18:00").do(scheduled_task)
schedule.every().wednesday.at("18:00").do(scheduled_task)
schedule.every().thursday.at("18:00").do(scheduled_task)
schedule.every().friday.at("18:00").do(scheduled_task)

while True:
    schedule.run_pending()
    time.sleep(1)