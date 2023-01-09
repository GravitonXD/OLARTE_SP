import pickle
import numpy as np
import json
import os

from utils import stock_symbols as ss

"""
    This python file contains functions neecessary for processing
    the collected data using the Machine Learning models.
"""


# This function will load a model based on the path and model_name provided
def load_model(model_name: str, path="./ml_model/"):
    model_path = f"{path}{model_name}.joblib"
    return pickle.load(open(model_path, "rb"))

# This function will allow us to iterate through the 20 stock data files 
#   and predict their future movement using the loaded model
def process_data(loaded_model: str, predict_len=10):
    # Iterate through the 20 stock data files from /data/db/stock_data/{stock_symbol}.csv
    stock_symbols = ss.get_stock_symbols()
    # Appeend PSEI to the list of stock symbols
    stock_symbols.append("PSEI")

    # Initialize the dictionary that will hold the processed data
    # key = stock symbol
    # value = (last actual cloaing, list of predictions with length=predict_len)
    processed_data = {stock:[] for stock in stock_symbols}

    # Iterate through the stock symbols
    for stock in stock_symbols:
        predicted_closings = []
        stock_data = np.loadtxt(f"./data/db/stock_data/{stock}.csv", delimiter=",")
        # Only get the closing price, which is at the 4th index
        stock_data = stock_data[:, 4]
        # From stock_data, use the loaded model to predict a len=predict_len number of predictions
        for _ in range(predict_len):
            predicted_closing = loaded_model.predict(stock_data.reshape(-1, 1))
            predicted_closings.append(predicted_closing[-1])
            stock_data = np.append(stock_data, predicted_closing)
        # Append the tiple of last actual closing , and list of predictions 
        #   to the processed_data dictionary
        last_actual = stock_data[-1]
        processed_data[stock] = tuple(last_actual, predicted_closings)
    
    return processed_data


# This function will return two dictionaries
#   one for the stocks to buy and one for the stocks to sell.
# Note: Minimum_score determines the minimum difference in 
#   between two consecutive stock prices to be considered advantageous to buy
#   By default it is set to 10% or 0.1
def post_processing(processed_data, minimum_score=0.1):
    stock_symbols = ss.get_stock_symbols()

    # Dictionary containing the last acutaul closing price of each stock
    last_actual_closing = {stock:processed_data[stock][0] for stock in stock_symbols}
    
    # Initialize the dictionaries for the stocks to buy and stocks to sell
    stocks_to_buy = {}
    stocks_to_sell = {}

    # Iterate through the processed data
    for stock in stock_symbols:
        predictions = processed_data[stock][1]
        # Calculate the percentile increase form last actual closing to the last prediction
        #   and add it to the stocks_to_buy or stocks_to_sell dictionary
        #   depending on the value of the percentile increase
        percentile_increase = (predictions[-1] - last_actual_closing[stock]) / last_actual_closing[stock]
        if percentile_increase > minimum_score:
            stocks_to_buy[stock] = processed_data[stock]
        else:
            stocks_to_sell[stock] = processed_data[stock]
    
    return stocks_to_buy, stocks_to_sell