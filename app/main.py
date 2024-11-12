from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def healt_check():
    return "It is working!"