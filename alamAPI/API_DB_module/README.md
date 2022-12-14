# STOCK MARKET PRICE FORECASTING (SMPF) MODULE
Employ SMPF Model

# Creation of Virtual Environment
Create a virtual environment by following this commands:
1. [INSTALLATION] virtualenv venv
note: make sure to pip install virtualenv first
2. [RUN_VIRTUAL_ENVIRONMENT] source venv/bin/activate
note: Commands are for Linux System

# FASTAPI INSTALLATION
To install FastAPI: https://fastapi.tiangolo.com/
3. pip install fastapi

# UVICORN INSTALLATION AND USAGE
4. pip install uvicorn
5. cd SMPF[api]
6. uvicorn main:app --reload
7. Check browser on localhost:8000

# MONGODB INSTALLATION AND SETUP
8. Visit: https://www.mongodb.com/docs/manual/installation/
For Linux: https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/
9. Start MongoDB server : sudo service mongod start
Note: FOR WSL, the command may not work so run it manually using: 
sudo /usr/bin/mongod --fork --config /etc/mongod.conf
10. Install GUI (MongoDB Compass) : https://www.mongodb.com/products/compass

# MONGOENGINE INSTALLATION AND SETUP
11. pip install mongoengine