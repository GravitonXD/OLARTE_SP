"""

    This script will process the data and create the json files
    for the stock to buy and stock to sell, which will be passed to the database.

"""
# Import local modules
from utils import db_actions
from utils import logs_and_alerts as la
import ml_processor as mp
import json
from os import makedirs

def main():
    # Directory for the logs
    log_directory = "data_processor_logs"
    try:
        # MACHINE LEARNING APPLICATION
        model_names = ["dmd_lstm"]

        # Loop through the models to generate a buy and sell list
        buy_list = []
        sell_list = []
        for model in model_names:
            # Load the model
            try:
                loaded_model = mp.load_model(model)
                la.Logs().success_log(f"Successfully loaded model: {model}", log_directory)
                la.Alerts().success_alert(f"Successfully loaded model: {model}")
            except:
                la.Logs().error_log(f"Failed to load model: {model}", log_directory)
                la.Alerts().error_alert(f"Failed to load model: {model}. Program will exit")
                exit(1)
            # Process the data using the model
            try:
                processed_data = mp.process_data(loaded_model)
                la.Logs().success_log(f"Successfully processed data for model: {model}", log_directory)
                la.Alerts().success_alert(f"Successfully processed data for model: {model}")
            except:
                la.Logs().error_log(f"Failed to process data for model: {model}", log_directory)
                la.Alerts().error_alert(f"Failed to process data for model: {model}. Program will exit")
                exit(1)
            # Post process the data
            try:
                stocks_to_buy, stocks_to_sell = mp.post_processing(processed_data)
                la.Logs().success_log(f"Successfully processed data for model: {model}", log_directory)
                la.Alerts().success_alert(f"Successfully processed data for model: {model}")
            except:
                la.Logs().error_log(f"Failed to process data for model: {model}", log_directory)
                la.Alerts().error_alert(f"Failed to process data for model: {model}. Program will exit")
                exit(1)

            # Save the stocks to buy and stocks to sell to json files in utils/json_data
            try:
                for stock in stocks_to_buy:
                    preJSON = {
                        "stock_symbol": stocks_to_buy[stock],
                        "last_closing": stocks_to_buy[stock][0],
                        "predicted_closing": {str(model): stocks_to_buy[stock][1]}
                    }
                    buy_list.append(preJSON)
                la.Logs().success_log(f"Successfully saved stocks to buy for model: {model}", log_directory)
                la.Alerts().success_alert(f"Successfully saved stocks to buy for model: {model}")
            except:
                la.Logs().error_log(f"Failed to save stocks to buy for model: {model}", log_directory)
                la.Alerts().error_alert(f"Failed to save stocks to buy for model: {model}. Program will exit")
                exit(1)
            
            try:
                for stock in stocks_to_sell:
                    preJSON = {
                        "stock_symbol": stocks_to_sell[stock],
                        "last_closing": stocks_to_sell[stock][0],
                        "predicted_closing": {str(model): stocks_to_buy[stock][1]}
                    }
                    sell_list.append(preJSON)
                la.Logs().success_log(f"Successfully saved stocks to sell for model: {model}", log_directory)
                la.Alerts().success_alert(f"Successfully saved stocks to sell for model: {model}")
            except:
                la.Logs().error_log(f"Failed to save stocks to sell for model: {model}", log_directory)
                la.Alerts().error_alert(f"Failed to save stocks to sell for model: {model}. Program will exit")
                exit(1)


        # Save the buy and sell lists to their corresponding json files    
        try:
            with open("/preprocessor/utils/json_data/stocks2buy.json", "w") as f:
                    json.dump(buy_list, f)
            la.Logs().success_log(f"Successfully saved stocks to buy", log_directory)
            la.Alerts().success_alert(f"Successfully saved stocks to buy")
        except:
            la.Logs().error_log(f"Failed to save stocks to buy", log_directory)
            la.Alerts().error_alert(f"Failed to save stocks to buy. Program will exit")
            exit(1)

        try:
            with open("/preprocessor/utils/json_data/stocks2buy.json", "w") as f:
                    json.dump(sell_list, f)
            la.Logs().success_log(f"Successfully saved stocks to sell", log_directory)
            la.Alerts().success_alert(f"Successfully saved stocks to sell")
        except:
            la.Logs().error_log(f"Failed to save stocks to sell", log_directory)
            la.Alerts().error_alert(f"Failed to save stocks to sell. Program will exit")
            exit(1)
        
        la.Logs().success_log(f"Successfully applied machine learning model/s to collected data", log_directory)
        la.Alerts().success_alert(f"Successfully applied machine learning model/s to collected data")

    except Exception:
        la.Logs().error_log(f"Failed to apply machine learning model/s to collected data", log_directory)
        la.Alerts().error_alert(f"Failed to apply machine learning model/s to collected data. Program will exit")
        exit(1)

    try:
        # DATABASE ACTIONS
        db_actions.connect_to_db()
        db_actions.purge_buy()
        db_actions.purge_sell()
        db_actions.save_buy_from_json()
        db_actions.save_sell_from_json()
    except:
        pass

if __name__ == "__main__":
    main()
