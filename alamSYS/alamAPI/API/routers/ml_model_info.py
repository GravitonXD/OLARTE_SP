from fastapi import APIRouter
from DB_model.models import ML_Models_Info as Info
from datetime import datetime
import json

router = APIRouter(
    prefix="/ml_model_info",
    tags=["ML Model Info"],
)

# ===== ML MODEL INFO =====================================================
# Get all ML Model info
# This is a public endpoint and does not require authentication
@router.get("/all", tags=["ML Model Info"])
def get_all_stocks_info():
        # Get all data from the "Buy" collection
                data = Info.objects().to_json()
                json_data = json.loads(data)
                # Return the data and the current datetime
                return {
                        "All Stocks Info": json_data,
                        "Date and Time": datetime.now()
                }

# Get a specific ML Model info by model name
# This is a public endpoint and does not require authentication
@router.get("/{model_name}", tags=["ML Model Info"])
def get_stock_info(model_name: str):
        stock_code_query = model_name.upper()
        # Get stock info from the "Info" collection
        data = Info.objects(stock_symbol=stock_code_query).to_json()
        json_data = json.loads(data)
        # Return the data and the current datetime
        return {
                # Rturn the stock info, if the stock code is not found, return "Stock not found"
                "Stock Info": json_data if json_data else "Stock not found",
                "Date and Time": datetime.now()
        }
# ===== END ML MODEL INFO =================================================