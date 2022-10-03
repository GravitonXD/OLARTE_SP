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
import pandas as pd
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


def save_historical_data(response, file_name, url, stock_symbol):
    # Check if the file exists
    # If it does, then append the data to the file
    # If it doesn't, then create the file and write the data to it
    file_action = "a" if os.path.exists(file_name) else "w"
    try:
        with open(file_name, file_action) as file:
            if file_action == "w":
                file.write(response.content)
            else:
                # Use the pandas library to read the CSV file, and check the last date
                df = pd.read_csv(file_name)
                last_date = df["Date"].iloc[-1]
                last_date = datetime.datetime.strptime(last_date, "%Y-%m-%d")

                # Compare the last date with the current date
                df = pd.read_csv(url)
                df = df[df["Date"] > last_date.strftime("%Y-%m-%d")]

                # Write the data to the file if not empty
                if df.empty:
                    ### LOG ###
                    # Log the error in the warning_log.txt file
                    action = "a" if os.path.exists("./module_logs/warning_log.txt") else "w"
                    with open("./module_logs/warning_log.txt", action) as error_log:
                        error_log.write(f"[WARNING]//{current_date()}::{log_time()}: No new data to appended to {file_name}\n")
                    error_log.close()

                    ### ALERT ###
                    # Alert the user that there is no new data to append to the file
                    print(f"{current_date()}::{log_time()}: \033[1;33m [WARNING] \033[m No new data to append to {file_name}")
                    # Exit the function
                    return

                # Append the data to the file
                df.to_csv(file, header=False, index=False)
        file.close()
    except:
        ### LOG ###
        # Log the error in the error_log.txt file
        action = "a" if os.path.exists("./module_logs/error_log.txt") else "w"
        with open("./module_logs/error_log.txt", action) as error_log:
            error_log.write(f"[ERROR]//{current_date}::{log_time()}: Saving/Update of historical data failed for {stock_symbol}\n")
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
            error_log.write(f"[ERROR]//{current_date()}::{log_time()}: API key not defined in the environment variable!\n")
        error_log.close()

        ### ALERT ###
        # Alert the user that the API key is not defined in the environment variable
        print(f"{current_date()}::{log_time()}: \033[1;31m [ERROR] \033[m API key not defined in the environment variable!\nSee error_log file for more details\nExiting...\n")
        exit()

    # Print Symbol List
    stock_symbols = sb.get_stock_symbols()
    
    # LOOP THROUGH THE STOCK SYMBOLS
    for stock_symbol in stock_symbols:
        url = f"https://eodhistoricaldata.com/api/eod/{stock_symbol}.PSE?api_token={API_KEY}&period=d"
        response = requests.get(url)
        file_name = f"./PHSM_historical_data/{stock_symbol}.csv"

        # Check if the response is successful
        if response.status_code == 200:
            save_historical_data(response, file_name, url, stock_symbol)

            ### LOG ###
            # Log the successful data collection in the success_log.txt file
            action = "a" if os.path.exists("./module_logs/success_log.txt") else "w"
            with open("./module_logs/success_log.txt", action) as success_log:
                success_log.write(f"[SUCCESS]//{current_date()}::{log_time()}: Successfully collected data for {stock_symbol}\n")

            ### ALERT ###
            # Alert the user that the data collection was successful
            print(f"{current_date()}::{log_time()}: \033[1;32m [SUCCESS] \033[m Successfully collected data for {stock_symbol}")

        else:
            ### LOG ###
            # Log the error in the error_log.txt file
            action = "a" if os.path.exists("./module_logs/error_log.txt") else "w"
            with open("./module_logs/error_log.txt", action) as error_log:
                error_log.write(f"[ERROR]//{current_date()}::{log_time()}: {response.status_code} - {response.reason}, Failed to get historical data of {stock_symbol}\n")
            error_log.close()

            ### ALERT ###
            # Alert the user that the data collection was unsuccessful
            print(f"{current_date()}::{log_time()}: \033[1;31m [ERROR] \033[m {response.status_code} - {response.reason}\nSee error_log file for more details\n\n")
    
    ### LOG ###
    # Log the successful completion of the Python Script in the success_log.txt file
    action = "a" if os.path.exists("./module_logs/success_log.txt") else "w"
    with open("./module_logs/success_log.txt", action) as success_log:
        success_log.write(f"[SUCCESS]//{current_date()}::{log_time()}: Successfully completed the PHSM_DataCollector Python Script\n")
    success_log.close()

    ### ALERT ###
    # Alert the user that the Python Script was successfully completed
    print(f"{current_date()}::{log_time()}: \033[1;32m [SUCCESS] \033[m Successfully completed the PHSMData Collector Module\n")
    print("------------------- EXITING PHSM_DC MAIN.PY ---------------------\n")
if __name__ == "__main__":
    main()