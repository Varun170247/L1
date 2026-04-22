import sys
import ast

def solve(expression):
    try:
        allowed_ops = {'add': '+', 'sub': '-', 'mul': '*', 'div': '/'}
        result = eval(expression, {"__builtins": {}}, {})
        return result
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        expr = " ".join(sys.argv[1:])
        print(f"Result: {solve(expr)}")
    else:
        print("Usage: python main.py <expression>")
        print("Example: python main.py 2 + 2")
        print("Example: python main.py 10 / 5 * 2")