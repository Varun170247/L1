from fastapi import FastAPI
from pydantic import BaseModel
import re
import math

app = FastAPI()

class Query(BaseModel):
    question: str

def solve(query):
    query = query.strip()
    
    patterns = [
        (r'What is (\d+)\s*\+\s*(\d+)\?', lambda a, b: f"The sum is {a + b}."),
        (r'What is (\d+)\s*-\s*(\d+)\?', lambda a, b: f"The difference is {a - b}."),
        (r'What is (\d+)\s*\*\s*(\d+)\?', lambda a, b: f"The product is {a * b}."),
        (r'What is (\d+)\s*/\s*(\d+)\?', lambda a, b: f"The quotient is {a / b}." if b != 0 else "Error: Division by zero."),
        (r'What is (\d+)\s*\^\s*(\d+)\?', lambda a, b: f"The result is {a ** b}."),
        (r'What is the square root of (\d+)\??', lambda a: f"The square root is {math.sqrt(int(a))}."),
        (r'What is (\d+)\s*\+\s*(\d+)\s*\+\s*(\d+)\?', lambda a, b, c: f"The sum is {a + b + c}."),
    ]
    
    for pattern, func in patterns:
        match = re.match(pattern, query, re.IGNORECASE)
        if match:
            try:
                nums = tuple(int(m) for m in match.groups())
                return func(*nums) if len(nums) > 1 else func(nums[0])
            except Exception as e:
                return f"Error: {e}"
    
    return "Could not understand the query."

@app.post("/v1/answer")
def get_answer(query: Query):
    return {"answer": solve(query.question)}

@app.get("/")
def home():
    return {"message": "Math Solver API", "endpoint": "/v1/answer"}
