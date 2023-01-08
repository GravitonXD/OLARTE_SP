from fastapi import APIRouter

router = APIRouter(
    prefix="/home",
    tags=["Home"],
)


# ====== HOME ==================================================
@router.get("/")
def home():
    return {"message": "Welcome to alamAPI an API for the Philippine Stock Market Price Trend Forecasting System, developed by John Markton M. Olarte"}
# ====== END HOME ==============================================