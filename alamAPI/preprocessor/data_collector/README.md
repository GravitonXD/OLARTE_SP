# PHSM Data Collector Module
This is one of the main modules of the SYS_NAME that is responsible for collecting the Philippine Stock Market Data.

Data is collected from the EODHD: https://eodhistoricaldata.com/


AUTHOR: JOHN MARKTON M. OLARTE

# main.py
This contains the main python script for this module.

## Logs
Both Success and Error from the processes in the main.py are stored in their corresponding log text files located at the ./module_logs

Success Logs: These are actions that are logged to have run successfuly.

Error Logs: These are actions that are logged to have run unsuccessfuly.

Warning Logs: These are actions that are logged to have no apparent effect to the system flow, but it is still a good idea to inform the user about it.

## Alerts
Alerts are printed in the terminal of the user while the main.py is running it will tell the user for Warnings, Errors, and Success Messages.

All Alerts are also stored respectively in their log files.

ALERT TYPE COLORS (ANSI Code):
😡 Red - Error (\033[1;31m ERROR \033[m)
🟢 Green - Success (\033[1;32m SUCCESS \033[m)
🟡 Yellow - Warning (\033[1;33m WARNING \033[m)

NOTE: This coloring can only work on powershell and unix terminals, Windows CMD will not output the color and will have strange chars instead.

## INSTRUCTIONS FOR SETTING UP THE API_KEY IN THE ENVIRONMENT VARIABLES
### FOR WINDOWS SYSTEM
Follow these steps: https://www.computerhope.com/issues/ch000549.htm

Name: EOD_API_KEY
Value: "Your API key from EODHD"

### FOR LINUX SYSTEM
Follow these steps: 

Name: EOD_API_KEY
Value: "Your API key from EODHD"


## Current Bugs
None