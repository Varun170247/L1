import sys
import re
import math
import json

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
    
    try:
        nums = re.findall(r'-?\d+\.?\d*', query)
        if nums:
            expr = ' + '.join(nums)
            result = eval(expr, {"__builtins__": {}}, {})
            return f"The result is {result}."
    except:
        pass
    
    return "Could not understand the query."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        print(solve(query))
    else:
        print("Usage: python main.py \"What is 10 + 15?\"")
        print("Supported queries:")
        print('  "What is 10 + 15?"')
        print('  "What is 20 - 5?"')
        print('  "What is 4 * 5?"')
        print('  "What is 20 / 4?"')
        print('  "What is 2 ^ 8?"')
        print('  "What is the square root of 16?"')
        print('  "What is 1 + 2 + 3?"')