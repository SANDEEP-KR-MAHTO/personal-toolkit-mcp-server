# tools/math_tools.py
import math


def basic_calculator(expression: str) -> dict:
    """
    Safely evaluate a math expression.
    Supports: +, -, *, /, **, %, sqrt, floor, ceil, abs, round
    Example: '2 + 3 * 4', 'sqrt(144)', '2 ** 10'
    """
    allowed_names = {
        "sqrt": math.sqrt,
        "floor": math.floor,
        "ceil": math.ceil,
        "abs": abs,
        "round": round,
        "pi": math.pi,
        "e": math.e,
        "log": math.log,
        "log10": math.log10,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
    }
    try:
        result = eval(expression, {"__builtins__": {}}, allowed_names)  # noqa: S307
        return {"expression": expression, "result": result}
    except Exception as ex:
        return {"expression": expression, "error": str(ex)}


def unit_converter(value: float, from_unit: str, to_unit: str) -> dict:
    """
    Convert between common units.
    Supported:
      Length:      km, m, cm, mm, miles, yards, feet, inches
      Weight:      kg, g, mg, lb, oz
      Temperature: celsius, fahrenheit, kelvin
    """
    # --- Length conversions (base: meters) ---
    length_to_meters = {
        "km": 1000, "m": 1, "cm": 0.01, "mm": 0.001,
        "miles": 1609.344, "yards": 0.9144, "feet": 0.3048, "inches": 0.0254,
    }
    # --- Weight conversions (base: grams) ---
    weight_to_grams = {
        "kg": 1000, "g": 1, "mg": 0.001, "lb": 453.592, "oz": 28.3495,
    }

    fu, tu = from_unit.lower(), to_unit.lower()

    # Temperature (special case)
    if fu in ("celsius", "fahrenheit", "kelvin") or tu in ("celsius", "fahrenheit", "kelvin"):
        if fu == "celsius" and tu == "fahrenheit":
            result = (value * 9 / 5) + 32
        elif fu == "fahrenheit" and tu == "celsius":
            result = (value - 32) * 5 / 9
        elif fu == "celsius" and tu == "kelvin":
            result = value + 273.15
        elif fu == "kelvin" and tu == "celsius":
            result = value - 273.15
        elif fu == "fahrenheit" and tu == "kelvin":
            result = (value - 32) * 5 / 9 + 273.15
        elif fu == "kelvin" and tu == "fahrenheit":
            result = (value - 273.15) * 9 / 5 + 32
        else:
            result = value  # same unit
        return {"value": value, "from": fu, "to": tu, "result": round(result, 6)}

    # Length
    if fu in length_to_meters and tu in length_to_meters:
        result = value * length_to_meters[fu] / length_to_meters[tu]
        return {"value": value, "from": fu, "to": tu, "result": round(result, 6)}

    # Weight
    if fu in weight_to_grams and tu in weight_to_grams:
        result = value * weight_to_grams[fu] / weight_to_grams[tu]
        return {"value": value, "from": fu, "to": tu, "result": round(result, 6)}

    return {"error": f"Unsupported unit pair: '{from_unit}' → '{to_unit}'"}


def prime_check(n: int) -> dict:
    """Check whether a number is prime and return its factors."""
    if n < 2:
        return {"number": n, "is_prime": False, "factors": []}
    factors = []
    temp = n
    for i in range(2, int(math.sqrt(n)) + 1):
        while temp % i == 0:
            factors.append(i)
            temp //= i
    if temp > 1:
        factors.append(temp)
    return {"number": n, "is_prime": len(factors) == 1 and factors[0] == n, "factors": factors}
