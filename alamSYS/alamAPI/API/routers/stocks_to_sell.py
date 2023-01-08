from fastapi import APIRouter
from DB_model.models import Sell
from datetime import datetime
import json

router = APIRouter(
    prefix="/stocks_to_sell",
    tags=["Stocks to Sell"],
)


# ===== STOCKS TO SELL ==================================================
# get all stocks to sell
# This is a public endpoint and does not require authentication
@router.get("/all", tags=["Stocks to Sell"])
def get_all_stocks_to_sell():
    # Get all data from the "Buy" collection
        data = Sell.objects().to_json()
        json_data = json.loads(data)
        # Return the data and the current datetime
        return {
                "All Stocks to Sell": json_data,
                "Date and Time": datetime.now()
        }
# ===== END STOCKS TO SELL ===============================================
