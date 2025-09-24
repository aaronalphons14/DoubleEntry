from fastapi import FastAPI, APIRouter
from transactions.routes import transac_router
from transactions.database import init_transac_db

app=FastAPI()

wow=APIRouter()
app.include_router(transac_router, prefix="/transaction")

init_transac_db()

@wow.get("/")
def read_root():
    return {"message":"Hello World!"}

app.include_router(wow, prefix="/wow")

