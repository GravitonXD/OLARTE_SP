from fastapi import APIRouter
from DB_model.models import Info
from datetime import datetime
import json

router = APIRouter(
    prefix="/stocks_info",
    tags=["Stocks Info"],
)


# ===== STOCKS INFO =====================================================
# Get all stocks info
# This is a public endpoint and does not require authentication
@router.get("/all", tags=["Stocks Info"])
def get_all_stocks_info():
        # Get all data from the "Buy" collection
                data = Info.objects().to_json()
                json_data = json.loads(data)
                # Return the data and the current datetime
                return {
                        "All Stocks Info": json_data,
                        "Date and Time": datetime.now()
                }

# Get a specific stock info
# This is a public endpoint and does not require authentication
@router.get("/{stock_code}", tags=["Stocks Info"])
def get_stock_info(stock_code: str):
        stock_code_query = stock_code.upper()
        # Get stock info from the "Info" collection
        data = Info.objects(stock_symbol=stock_code_query).to_json()
        json_data = json.loads(data)
        # Return the data and the current datetime
        return {
                # Rturn the stock info, if the stock code is not found, return "Stock not found"
                "Stock Info": json_data if json_data else "Stock not found",
                "Date and Time": datetime.now()
        }
# ===== END STOCKS INFO =================================================