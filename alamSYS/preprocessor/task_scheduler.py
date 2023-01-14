import schedule
import time

# Local Imports
from data_collector import collector
from data_processor import process
from utils import init_db
from utils import logs_and_alerts as la

def status_update():
    # Print rthe current time
    print(f"[STATUS UPDATE] {time.ctime()} :: Task Scheduler still running...")

def scheduled_task():
    log_directory = "scheduled_task_logs"

    print("----------------STARTING SCHEDULED TASK----------------------")
    la.Logs().success_log("Scheduled task has successfully started", log_directory)
    la.Alerts().success_alert("Scheduled task has successfully started")

    try:
        # Run data collector module
        collector.main()
        # Run trained ML model
        process.main()

        print("----------------SCHEDULED TASK COMPLETED----------------------")
        la.Logs().success_log("Scheduled task has successfully completed", log_directory)
        la.Alerts().success_alert("Scheduled task has successfully completed")

    except:
        print("Preprocessesing failed see data logs for more details")
        la.Logs().error_log("Scheduled task has failed", log_directory)
        la.Alerts().error_alert("Scheduled task has failed")

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