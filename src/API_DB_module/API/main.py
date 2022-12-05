# Python Imports
from fastapi import FastAPI
from mongoengine import connect
import json
from datetime import datetime
import os

# Import models
from DB_model.models import Buy
from DB_model.models import Sell
from DB_model.models import Info

# Create the FastAPI app
app = FastAPI(
        title="alamAPI",
        description="""alamAPI is an API for the Philippine Stock Market Price Trend Forecasting System (SMPTF System)
                        \nThis project is part of the requirements for the completion of BS Computer Science at the University of the Philippines Visayas
                        \nDeveloped solely by: John Markton M. Olarte""",
        version="1.0.0",
        docs_url="/alamAPI/v1/docs",
        openapi_url="/alamAPI/v1/openapi.json",
        redoc_url="/alamAPI/v1/redoc",
        contact={
                "name": "John Markton M. Olarte",
                "email": "jmolarte@up,edu.ph"
        },
        openapi_tags=[
                {
                        "name": "Home",
                        "description": "This API endpoint outputs a welcome message. Which should inform the user that they have successfully connected to the alamAPI."
                },
                {
                        "name": "Stocks to Buy",
                        "description": "This API endpoint outputs a list of stocks to buy based from the current market price and the predicted price up-trend."
                },
                {
                        "name": "Stocks to Sell",
                        "description": "This API endpoint outputs a list of stocks to sell based from the current market price and the predicted price down-trend."
                },
                {
                        "name": "Stocks Info",
                        "description": "This API endpoint outputs a list of stocks included in the Philippine Stock Market Price Trend Forecasting System and their corresponding information."
                }
        ]
)
# Connect to the database, using the environment variables (set in the docker-compose.yml file)
connect(db=os.environ['MONGO_INITDB_DATABASE'], host=os.environ['MONGO_HOST'], port=int(os.environ['MONGO_PORT']))

# Current datetime
def _current_datetime():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ROOT
@app.get("/", tags=["Home"])
def home():
    return {"message": "Welcome to alamAPI an API for the Philippine Stock Market Price Trend Forecasting System, developed by John Markton M. Olarte"}

# ====== STOCKS TO BUY ==================================================
# Get all stocks to buy
# This is a public endpoint and does not require authentication
@app.get("/stocks_to_buy/all", tags=["Stocks to Buy"])
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
@app.get("/stocks_to_sell/all", tags=["Stocks to Sell"])
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


# ===== STOCKS INFO =====================================================
# Get all stocks info
# This is a public endpoint and does not require authentication
@app.get("/stocks_info/all", tags=["Stocks Info"])
def get_all_stocks_info():
        # Get all data from the "Buy" collection
                data = Info.objects().to_json()
                json_data = json.loads(data)
                # Return the data and the current datetime
                return {
                        "All Stocks Info": json_data,
                        "Last Updated": _current_datetime()
                }
# ===== END STOCKS INFO =================================================

if __name__ == "__main__":
    # Run the app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)