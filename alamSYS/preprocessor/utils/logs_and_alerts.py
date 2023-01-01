"""
A Python module for logging and alerting.
"""

import datetime
from os import path
from os import makedirs

class Logs:
    def __init__(self):
        self.logs = ""
        self.date = datetime.date.today().strftime("%Y-%m-%d")
        self.time = datetime.datetime.now().strftime("%H:%M:%S")
    
    def success_log(self, message, log_directory):
        # Log Format: Date, Time, Message
        self.logs = f"{self.date}, {self.time}, {message}\n"
        # Define the action to be taken (If no file exists, create a new file)
        action = "a" if path.exists("/data/db/data-collector_logs/success_log.csv") else "w"
        # Create the folder if it does not exist
        makedirs(f"/data/db/{log_directory}/", exist_ok=True)
        with open(f"/data/db/{log_directory}/success_log.csv", action) as success_log:
            # Write the log to the file
            success_log.write(self.logs)
        # Close the file
        success_log.close()
    
    def error_log(self, message, log_directory):
        # Log Format: Date, Time, Message
        self.logs = f"{self.date}, {self.time}, {message}\n"
        # Define the action to be taken (If no file exists, create a new file)
        action = "a" if path.exists("/data/db/data-collector_logs/error_log.csv") else "w"
        # Create the folder if it does not exist
        makedirs(f"/data/db/{log_directory}/", exist_ok=True)
        with open(f"/data/db/{log_directory}/error_log.csv", action) as error_log:
            # Write the log to the file
            error_log.write(self.logs)
        # Close the file
        error_log.close()

class Alerts(Logs):
    def __init__(self):
        super().__init__()
    
    def success_alert(self, message):
        # Alert Format: [SUCCESS] Date Time: Message
        print(f" \033[1;32m [SUCCESS] \033[m{self.date} {self.time} : {message}")
    
    def error_alert(self, message):
        # Alert Format: [ERROR] Date Time: Message
        print(f" \033[1;31m [ERROR] \033[m{self.date} {self.time} : {message}")



