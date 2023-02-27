import numpy as np
from tensorflow import keras

from utils import stock_symbols as ss

"""
    This python file contains functions neecessary for processing
    the collected data using the Machine Learning models.
"""


# This function will load a model based on the path and model_name provided
def load_model(model_name: str, path="/preprocessor/data_processor/ml_model"):
    model_path = f"{path}/{model_name}.keras"
    loaded_model = keras.models.load_model(model_path)
    return loaded_model
        

# This function will allow us to iterate through stock data files 
#   and predict their future movement using the loaded model
def process_data(loaded_model, model_name:str, len_predictions:int=5):
    # Iterate through the 20 stock data files from /data/db/stock_data/{stock_symbol}.csv
    stock_symbols = ss.get_stock_symbols()
    # Appeend PSEI to the list of stock symbols
    stock_symbols.append("PSEI")

    # Initialize the dictionary that will hold the processed data
    # key = stock symbol
    # value = (last actual closing, list of predictions with length=predict_len)
    processed_data = {stock:[] for stock in stock_symbols}

    # Iterate through the stock symbols
    for stock in stock_symbols:
        predicted_closings = []
        
        # Initialize the closing prices of the stock
        closing_prices = np.array([])
        # Get the last closing prices based on the window size of the model
        window_size = loaded_model.count_params() - 1
        closing_prices = np.genfromtxt(f'/data/db/stock_data/{stock}.csv',
                                        delimiter=',',
                                        skip_header=1,
                                        usecols=4)
        closing_prices = closing_prices[-(window_size):]
        # Get the last actual closing price
        last_actual = closing_prices[-1]

        """
            PREDICTED CLOSINGS:
                1st Prediction: input[closing_prices]
                2nd Prediction: input[closing_prices[-4:], pred]
                3rd Prediction: input[closing_prices[-3:], pred]
                4th Prediction: input[closing_prices[-2:], pred]
                5th Prediction: input[closing_prices[-1:], pred]
        """
        for _ in range(len_predictions):
            data = np.append(closing_prices, predicted_closings)
            prediction = loaded_model.predict(data[-(window_size):].reshape(1,5))
            predicted_closings.append(float(prediction))

        processed_data[stock] = tuple((last_actual, {model_name: predicted_closings}))

    return processed_data


# This function will return two dictionaries
#   one for the stocks to buy and one for the stocks to sell.
# Note: Minimum_score determines the minimum difference in 
#   between two consecutive stock prices to be considered advantageous to buy
#   By default it is set to 0.01 or 1%
def post_processing(processed_data, model_name:str, minimum_score:float=0.01):
    stock_symbols = ss.get_stock_symbols()
    # Appeend PSEI to the list of stock symbols
    stock_symbols.append("PSEI")

    # Dictionary containing the last acutaul closing price of each stock
    last_actual_closing = {stock:processed_data[stock][0] for stock in stock_symbols}
    
    # Initialize the dictionaries for the stocks to buy and stocks to sell
    stocks_to_buy = {}
    stocks_to_sell = {}

    # Iterate through the processed data
    for stock in stock_symbols:
        predictions = processed_data[stock][1][model_name]
        # Calculate the percentile increase form last actual closing to the last prediction
        #   and add it to the stocks_to_buy or stocks_to_sell dictionary
        #   depending on the value of the percentile increase
        percentile_increase = (predictions[-1] - last_actual_closing[stock]) / last_actual_closing[stock]
        if percentile_increase > minimum_score:
            stocks_to_buy[stock] = processed_data[stock]
        else:
            stocks_to_sell[stock] = processed_data[stock]
    
    return stocks_to_buy, stocks_to_sell