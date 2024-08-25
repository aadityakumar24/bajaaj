from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

# Define a data model for the POST request
class DataInput(BaseModel):
    data: List[str] = Field(..., example=["M", "1", "334", "4", "B", "Z", "a"])

# Helper function to process data
def process_data(data):
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    lowercase_alphabets = [item for item in alphabets if item.islower()]
    highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None
    return numbers, alphabets, highest_lowercase_alphabet

@app.post("/bfhl")
async def bfhl_post(input_data: DataInput):
    user_id = "john_doe_17091999"  # Replace with actual logic if needed
    email = "john@xyz.com"  # Replace with actual logic if needed
    roll_number = "ABCD123"  # Replace with actual logic if needed
    
    numbers, alphabets, highest_lowercase_alphabet = process_data(input_data.data)
    
    return {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }

@app.get("/bfhl")
async def bfhl_get():
    return {"operation_code": 1}

# Exception handling
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return {"detail": str(exc.detail), "status_code": exc.status_code}

