# Python Imports
from fastapi import FastAPI
from mongoengine import connect

# Local imports
from endpoints.stocks2buy_endpoints import Stocks2BuyEndpoints
from endpoints.stocks2sell_endpoints import Stocks2SellEndpoints

# Create the FastAPI app
app = FastAPI()
# Connect to the database
connect(db="smpf", host="0.0.0.0", port=27017)

# ROOT
@app.get("/")
def home():
    return {"message": "Welcome to Stock Market Price Forecasting API developed by John Markton M. Olarte"}

# ====== STOCKS TO BUY ==================================================
# Get all stocks to buy
# This is a public endpoint and does not require authentication
@app.get("/stocks_to_buy/all")
def get_all_stocks_to_buy():
    return Stocks2BuyEndpoints().get_all_stocks_to_buy()
# ====== END STOCKS TO BUY ==============================================

# ===== STOCKS TO SELL ==================================================
# get all stocks to sell
# This is a public endpoint and does not require authentication
@app.get("/stocks_to_sell/all")
def get_all_stocks_to_sell():
    return Stocks2SellEndpoints().get_all_stocks_to_sell()
# ===== END STOCKS TO SELL ===============================================


# Run the app using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)