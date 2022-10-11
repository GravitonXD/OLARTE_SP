# Python Imports
from fastapi import FastAPI
from mongoengine import connect
import json
from datetime import datetime
import os

# Import models
from DB_model.models import Buy
from DB_model.models import Sell

# Create the FastAPI app
app = FastAPI()
# Connect to the database, using the environment variables (set in the docker-compose.yml file)
connect(db=os.environ['MONGO_INITDB_DATABASE'], host=os.environ['MONGO_HOST'], port=int(os.environ['MONGO_PORT']))

# Current datetime
def _current_datetime():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ROOT
@app.get("/")
def home():
    return {"message": "Welcome to Stock Market Price Forecasting API developed by John Markton M. Olarte"}

# ====== STOCKS TO BUY ==================================================
# Get all stocks to buy
# This is a public endpoint and does not require authentication
@app.get("/stocks_to_buy/all")
def get_all_stocks_to_buy():
    # Get all data from the "Buy" collection
        data = Buy.objects().to_json()
        json_data = json.loads(data)
        # Return the data and the current datetime
        return {
                "All Stocks to Buy": json_data,
                "Last Updated": _current_datetime()
        }
# ====== END STOCKS TO BUY ==============================================

# ===== STOCKS TO SELL ==================================================
# get all stocks to sell
# This is a public endpoint and does not require authentication
@app.get("/stocks_to_sell/all")
def get_all_stocks_to_sell():
    # Get all data from the "Buy" collection
        data = Sell.objects().to_json()
        json_data = json.loads(data)
        # Return the data and the current datetime
        return {
                "All Stocks to Sell": json_data,
                "Last Updated": _current_datetime()
        }
# ===== END STOCKS TO SELL ===============================================

if __name__ == "__main__":
    # Run the app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)