#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        return None
    except Exception as e:
        print("An error occurred: {}".format(e))
        return None
    finally:
        print("Inside result: {}".format(result))
        return result
    
# numerator = 10
# denominator = 0
# result = safe_print_division(numerator, denominator)

# if result is not None:
#     print(f"The division result is: {result}")