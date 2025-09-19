from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title = "calculator API")

class Operation(BaseModel):
    a: float
    b: float

@app.post("/add")
def add(op: Operation):
    return {"result": op.a + op.b}

@app.post("/subtract")
def subtract(op: Operation):
    return {"result": op.a - op.b}

@app.post("/multiply")
def multiply(op: Operation):
    return {"result": op.a * op.b}

@app.post("/divide")
def divide(op: Operation):
    if op.b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": op.a / op.b}
