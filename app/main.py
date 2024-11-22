from fastapi import FastAPI
from app.routes import router

app = FastAPI()

@app.get("/")
def healt_check():
    return "It is working!"


app.include_router(router)