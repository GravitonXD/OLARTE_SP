""""
    
    This Python Script will be used to collect historical data from the 
    Philippine Stock Market (PHSM) using the data provided by EODHD.

    EODHD: https://eodhistoricaldata.com/

    The data will be stored in a CSV file for further analysis.

    Author: JOHN MARKTON M. OLARTE
    Last Modified: October 02, 2022

"""

# Importing the necessary modules
import requests
import datetime
import os
import tools.stock_symbols as sb

def get_APIKey():
    # Get the API key as defined from the environment variable
    # NOTE: Please define the API key in the environment variable as EOD_API_KEY
    API_KEY = os.environ.get("EOD_API_KEY")
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

        ### LOG ###
        # Log the successful data collection in the success_log.txt file
        action = "a" if os.path.exists("./module_logs/success_log.txt") else "w"
        with open("./module_logs/success_log.txt", action) as success_log:
            success_log.write(f"[SUCCESS] {current_date()}::{log_time()}: Successfully collected data for {stock_symbol}.\n")
        success_log.close()

        ### ALERT ###
        # Alert the user that the data collection was successful
        print(f"{current_date()}::{log_time()}: \033[1;32m [SUCCESS] \033[m Successfully collected data for {stock_symbol}.\n")
    except:
        ### LOG ###
        # Log the error in the error_log.txt file
        action = "a" if os.path.exists("./module_logs/error_log.txt") else "w"
        with open("./module_logs/error_log.txt", action) as error_log:
            error_log.write(f"[ERROR] {current_date}::{log_time()}: Saving/Update of historical data failed for {stock_symbol}\n")
        error_log.close()

        ### ALERT ###
        # Alert the user that the saving/update of the historical data failed
        print(f"{current_date()}::{log_time()}: \033[1;31m [ERROR] \033[m Saving/Update of historical data failed for {stock_symbol}")



def main():
    print("------------------- STARTING PHSM_DC MAIN.PY ---------------------\n")
    # Check if the API key is defined in the environment variable
    try:
        API_KEY = get_APIKey()
    except:
        ### LOG ###
        # Log the API key error in the error_log.txt file
        # Check if the error_log file exists
        action = "a" if os.path.exists("./module_logs/error_log.txt") else "w"
        with open("./module_logs/error_log.txt", action) as error_log:
            error_log.write(f"[ERROR] {current_date()}::{log_time()}: API key not defined in the environment variable!\n")
        error_log.close()

        ### ALERT ###
        # Alert the user that the API key is not defined in the environment variable
        print(f"{current_date()}::{log_time()}: \033[1;31m [ERROR] \033[m API key not defined in the environment variable!\nSee error_log file for more details\nExiting...\n")
        exit()

    # Print Symbol List
    # TODO: Change to sb.get_stock_symbols() for production
    stock_symbols = sb.get_test_symbols()
    
    # LOOP THROUGH THE STOCK SYMBOLS
    for stock_symbol in stock_symbols:
        url = f"https://eodhistoricaldata.com/api/eod/{stock_symbol}.PSE?api_token={API_KEY}&period=d"
        response = requests.get(url)
        file_name = f"./PHSM_historical_data/{stock_symbol}.csv"

        # Check if the response is successful
        if response.status_code == 200:
            ### LOG ###
            # Log the successful request in the success_log.txt file
            action = "a" if os.path.exists("./module_logs/success_log.txt") else "w"
            with open("./module_logs/success_log.txt", action) as success_log:
                success_log.write(f"[SUCCESS] {current_date()}::{log_time()}: Request to get {stock_symbol} historical data was successful\n")

            ### ALERT ###
            # Alert the user that the request was successful
            print(f"{current_date()}::{log_time()}: \033[1;32m [SUCCESS] \033[m Request to get {stock_symbol} historical data was successful")

            # Save the data in a CSV file
            save_historical_data(response, file_name, stock_symbol)
        else:
            ### LOG ###
            # Log the error in the error_log.txt file
            action = "a" if os.path.exists("./module_logs/error_log.txt") else "w"
            with open("./module_logs/error_log.txt", action) as error_log:
                error_log.write(f"[ERROR] {current_date()}::{log_time()}: {response.status_code} - {response.reason}, Failed to get historical data of {stock_symbol}\n")
            error_log.close()

            ### ALERT ###
            # Alert the user that the data collection was unsuccessful
            print(f"{current_date()}::{log_time()}: \033[1;31m [ERROR] \033[m {response.status_code} - {response.reason}\nSee error_log file for more details\n\n")
    
    ### LOG ###
    # Log the successful completion of the Python Script in the success_log.txt file
    action = "a" if os.path.exists("./module_logs/success_log.txt") else "w"
    with open("./module_logs/success_log.txt", action) as success_log:
        success_log.write(f"[SUCCESS] {current_date()}::{log_time()}: Successfully completed the PHSM_DataCollector Python Script\n")
    success_log.close()

    ### ALERT ###
    # Alert the user that the Python Script was successfully completed
    print(f"{current_date()}::{log_time()}: \033[1;32m [SUCCESS] \033[m Successfully completed the PHSMData Collector Module\n")
    print("------------------- EXITING PHSM_DC MAIN.PY ---------------------\n")


if __name__ == "__main__":
    main()