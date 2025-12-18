from fastapi import FastAPI
from src.utils import add

app = FastAPI(title="My Application")

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/add")
def add_numbers(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": add(a, b)
    }
