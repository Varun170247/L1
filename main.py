import sys
import math
import cmath

def solve(expression):
    try:
        safe_dict = {
            'abs': abs, 'round': round, 'min': min, 'max': max,
            'sqrt': math.sqrt, 'cbranch': cmath.sqrt,
            'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
            'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
            'sinh': math.sinh, 'cosh': math.cosh, 'tanh': math.tanh,
            'log': math.log, 'log10': math.log10, 'log2': math.log2,
            'exp': math.exp, 'pow': math.pow, 'ceil': math.ceil,
            'floor': math.floor, 'factorial': math.factorial,
            'gcd': math.gcd, 'degrees': math.degrees, 'radians': math.radians,
            'pi': math.pi, 'e': math.e, 'tau': math.tau,
        }
        expressions = expression.replace('^', '**')
        expressions = expressions.replace('√', 'sqrt')
        expressions = expressions.replace('sqrt(', 'math.sqrt(')
        result = eval(expressions, {"__builtins": {}}, safe_dict)
        if isinstance(result, complex):
            return str(result) if result.imag else float(result.real)
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
        print("  python main.py sqrt 16")
        print("  python main.py 5 ^ 2 + 3 ^ 2")
        print("  python main.py sin 0")
        print("  python main.py log 10")
        print("  python main.py sqrt(16) + sqrt(9)")
        print("  python main.py 50 * 20%")
        print("  python main.py factorial 5")
        print("  python main.py abs -5")
        print("  python main.py ceil 5.7")
        print("  python main.py floor 5.7")