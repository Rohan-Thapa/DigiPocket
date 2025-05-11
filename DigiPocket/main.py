from fastapi import FastAPI
from config.database import connect_db, close_db
from controller.auth_controller import router as auth_router
from controller.user_controller import router as user_router
from controller.merchant_controller import router as merchant_router
from controller.wallet_controller import router as wallet_router
from controller.transaction_controller import router as transaction_router

app = FastAPI()
app.add_event_handler("startup", connect_db)
app.add_event_handler("shutdown", close_db)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(merchant_router)
app.include_router(wallet_router)
app.include_router(transaction_router)