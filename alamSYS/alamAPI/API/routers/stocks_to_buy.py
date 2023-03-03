from fastapi import APIRouter
from DB_model.models import Buy
from datetime import datetime
import json

router = APIRouter(
    prefix="/stocks_to_buy",
    tags=["Stocks to Buy"],
)


# ====== STOCKS TO BUY ==================================================
# Get all stocks to buy
# This is a public endpoint and does not require authentication
@router.get("/all")
def get_all_stocks_to_buy():
    # Get all data from the "Buy" collection
        data = Buy.objects().to_json()
        json_data = json.loads(data)
        # Return the data and the current datetime
        return {
                "Stocks": json_data,
                "DateTime": datetime.now()
        }
# ====== END STOCKS TO BUY ==============================================
