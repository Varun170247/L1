import sys
import math

def solve(expression):
    try:
        result = eval(expression.replace('^', '**'), {"__builtins__": {}}, {})
        if isinstance(result, complex):
            return str(result) if result.imag else float(result.real)
        if isinstance(result, float) and result.is_integer():
            return int(result)
        return result
    except Exception:
        try:
            safe_dict = {name: getattr(math, name) for name in dir(math)}
            safe_dict['__builtins__'] = {}
            result = eval(expression.replace('^', '**'), {}, safe_dict)
            if isinstance(result, float) and result.is_integer():
                return int(result)
            return result
        except Exception as e:
            return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        expr = " ".join(sys.argv[1:])
        result = solve(expr)
        print(f"Result: {result}")
    else:
        print("Math Solver - Usage Examples:")
        print("  python main.py 2 + 2")
        print("  python main.py 10 / 5 * 2")
        print("  python main.py 2 ^ 8")
        print("  python main.py sqrt(16)")
        print("  python main.py sqrt(16) + sqrt(9)")
        print("  python main.py sin(0)")
        print("  python main.py log(10)")
        print("  python main.py factorial(5)")
        print("  python main.py abs(-5)")
        print("  python main.py ceil(5.7)")
        print("  python main.py floor(5.7)")