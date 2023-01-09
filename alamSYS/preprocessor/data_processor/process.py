"""

    This script will process the data and create the json files
    for the stock to buy and stock to sell, which will be passed to the database.

"""

# Importing the libraries

# Import local modules
from utils import db_actions
import ml_processor as mp
import json

def main():
    # MACHINE LEARNING APPLICATION
    model_names = ["sample_model"]

    # Loop through the models to generate a buy and sell list
    buy_list = []
    sell_list = []
    for model in model_names:
        loaded_model = mp.load_model(model)
        processed_data = mp.process_data(loaded_model)
        stocks_to_buy, stocks_to_sell = mp.post_processing(processed_data)

        # Save the stocks to buy and stocks to sell to json files in utils/json_data
        
        for stock in stocks_to_buy:
            preJSON = {
                "stock_symbol": stocks_to_buy[stock],
                "last_closing": stocks_to_buy[stock][0],
                "predicted_closing": {str(model): stocks_to_buy[stock][1]}
            }
            buy_list.append(preJSON)
        
        
        # Save the stocks to sell to json file
        for stock in stocks_to_sell:
            preJSON = {
                "stock_symbol": stocks_to_sell[stock],
                "last_closing": stocks_to_sell[stock][0],
                "predicted_closing": {str(model): stocks_to_buy[stock][1]}
            }
            sell_list.append(preJSON)
        
    # Save the buy and sell lists to their corresponding json files
    with open("./utils/json_data/stocks2buy.json", "w") as f:
            json.dump(buy_list, f)
    with open("./utils/json_data/stocks2sell.json", "w") as f:
            json.dump(sell_list, f)

    # DATABASE ACTIONS
    db_actions.connect_to_db()
    db_actions.purge_buy()
    db_actions.purge_sell()
    db_actions.save_buy_from_json()
    db_actions.save_sell_from_json()

if __name__ == "__main__":
    main()
