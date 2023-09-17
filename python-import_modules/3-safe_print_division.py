# #!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result

# Example usage:
# a = 10
# b = 2
# safe_print_division(a, b)

# a = 5
# b = 0
# safe_print_division(a, b)