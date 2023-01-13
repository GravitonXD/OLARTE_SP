""""
    
    This Python Script will be used to collect historical data from the 
    Philippine Stock Market (PHSM) using the data provided by EODHD.

    EODHD: https://eodhistoricaldata.com/

    The data will be stored in a CSV file for further analysis.

    Author: JOHN MARKTON M. OLARTE
    Last Modified: October 11, 2022

"""

# Importing the necessary modules
import requests
import datetime
import os
# importing modules from utils
from utils import stock_symbols as ss
from utils import logs_and_alerts as la

def get_API_Key():
    # Get the API key as defined from the environment variable
    # NOTE: Please define the API key in the environment variable as EOD_API_KEY
    #      Otherwise create a file named "API_KEY.txt" in the tools directory and place the API key in the file

    # Get the API key from the environment variable if it exists
    # Otherwise, get the API key from the APIKey.txt file
    if os.environ.get("EOD_API_KEY") != None:
        API_KEY = os.environ.get("EOD_API_KEY")
        return API_KEY

    with open("./tools/API_KEY.txt", "r") as f:
        API_KEY = f.read()
    f.close()
    return API_KEY


def current_date():
    # This function will return the current date in the format of YYYY-MM-DD
    return datetime.date.today().strftime("%Y-%m-%d")


def log_time():
    # This function will return the current time in the format of HH:MM:SS
    return datetime.datetime.now().strftime("%H:%M:%S")


def save_historical_data(response, file_name, stock_symbol):
    try:
        # Save the data in a CSV file
        with open(file_name, "w") as f:
            f.write(response.text)
        f.close()

        ### LOG AND ALERT ###
        message = f"Successfully collected historical data for {stock_symbol}"
        log_directory = "data_collector_logs"
        # Log the successful data collection in the success_log.txt file
        la.Logs().success_log(message, log_directory)
        # Alert the successful data collection
        la.Alerts().success_alert(message)
        ######################
    except:
        ### LOG AND ALERT ###
        message = f"Failed to save historical data for {stock_symbol}"
        log_directory = "data_collector_logs"
        # Log the failed data collection in the error_log.txt file
        la.Logs().error_log(message, log_directory)
        # Alert the failed data collection
        la.Alerts().error_alert(message)
        ######################


def main():
    # Initialize Reusable Variables
    log_directory = "data_collector_logs" # Directory for the logs

    # Make this directory under /data/db of the container
    os.makedirs("/data/db/stock_data/", exist_ok=True)
    
    print("------------------- STARTING DATA COLLECTOR MODULE ---------------------\n")
    # Log the start of the data collector module
    la.Logs().success_log("Data collector module has successfully started", log_directory)
    la.Alerts().success_alert("Data collector module has successfully started")

    # Check if the API key is defined in the environment variable
    try:
        API_KEY = get_API_Key()

        ### LOG AND ALERT ###
        message = "Successfully retrieved API key"
        # Log the successful API key retrieval in the success_log.txt file
        la.Logs().success_log(message, log_directory)
        # Alert the successful API key retrieval
        la.Alerts().success_alert(message)
        ######################
    except:
        ### LOG AND ALERT ###
        message = "Failed to retrieve API key"
        # Log the failed API key retrieval in the error_log.txt file
        la.Logs().error_log(message, log_directory)
        # Alert the failed API key retrieval
        la.Alerts().error_alert(message)
        ######################

        # Exit the program
        exit()

    # Get the list of stock symbols
    stock_symbols = ss.get_stock_symbols()
    
    # LOOP THROUGH THE STOCK SYMBOLS
    for stock_symbol in stock_symbols:
        url = f"https://eodhistoricaldata.com/api/eod/{stock_symbol}.PSE?api_token={API_KEY}&period=d"
        response = requests.get(url)
        file_name = f"/data/db/stock_data/{stock_symbol}.csv"

        # Check if the response is successful
        if response.status_code == 200:
            ### LOG AND ALERT ###
            message = f"Successfully collected historical data for {stock_symbol}"
            # Log the successful data collection in the success_log.txt file
            la.Logs().success_log(message, log_directory)
            # Alert the successful data collection
            la.Alerts().success_alert(message)
            ######################

            # Save the data in a CSV file
            save_historical_data(response, file_name, stock_symbol)

        else:
            ### LOG AND ALERT ###
            message = f"Failed to collect historical data for {stock_symbol} with status code {response.status_code}"
            # Log the failed data collection in the error_log.txt file
            la.Logs().error_log(message, log_directory)
            # Alert the failed data collection
            la.Alerts().error_alert(message)
            ######################
    
    # GET THE HISTORICAL DATA FOR THE PSEI
    url = f"https://eodhistoricaldata.com/api/eod/PSEI.INDX?api_token={API_KEY}&period=d"
    response = requests.get(url)

    # Check if the response is successful
    if response.status_code == 200:
        ### LOG AND ALERT ###
        message = "Successfully collected historical data for PSEI"
        # Log the successful data collection in the success_log.txt file
        la.Logs().success_log(message, log_directory)
        # Alert the successful data collection
        la.Alerts().success_alert(message)
        ######################

        # Save the data in a CSV file
        save_historical_data(response, "/data/db/stock_data/PSEI.csv", "PSEI")
    else:
        ### LOG AND ALERT ###
        message = f"Failed to collect historical data for PSEi with status code {response.status_code}"
        # Log the failed data collection in the error_log.txt file
        la.Logs().error_log(message, log_directory)
        # Alert the failed data collection
        la.Alerts().error_alert(message)
        ######################
    
    ### LOG AND ALERT ###
    message = "Data Collector Module Finished"
    # Log the successful data collection in the success_log.txt file
    la.Logs().success_log(message, log_directory)
    # Alert the successful data collection
    la.Alerts().success_alert(message)
    ######################
    print("------------------- EXITING DATA COLLECTOR MODULE ---------------------\n")