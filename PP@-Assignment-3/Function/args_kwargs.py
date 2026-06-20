# ==========================================
# 1. *args (Positional Arguments)
# ==========================================

# Definition:
""""*args allows a function to accept any number of positional arguments, which are packed into a tuple inside the function.""""

def multiply_numbers(*args):
    """
    Takes any number of numeric arguments and returns their product.
    The variable 'args' acts as a tuple: (2, 3) or (2, 3, 4, 5)
    """
    total = 1
    
    # Loop through the tuple of arguments
    for number in args:
        total *= number
        
    return total

# Example usage for *args:
print("--- Testing *args ---")
print(multiply_numbers(2, 3))        # Output: 6
print(multiply_numbers(2, 3, 4, 5))  # Output: 120
print()


# ==========================================
# 2. **kwargs (Keyword Arguments)
# ==========================================

# Definition:
""""**kwargs allows a function to accept any number of keyword (named) arguments, which are packed into a dictionary inside the function.""""

def print_user_profile(**kwargs):
    """
    Takes arbitrary keyword arguments and prints them.
    The variable 'kwargs' acts as a dictionary: {'username': 'coder123', ...}
    """
    # Loop through the dictionary key-value pairs
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

# Example usage for **kwargs:
print("--- Testing **kwargs ---")
print_user_profile(username="coder123", role="Developer")
# Output:
# Username: coder123
# Role: Developer

print("-" * 20)

print_user_profile(name="Alex", age=28, country="Kazakhstan")
# Output:
# Name: Alex
# Age: 28
# Country: Kazakhstan
print()


# ==========================================
# 3. Combining Them Together
# ==========================================

def master_function(standard_arg, *args, **kwargs):
    """
    Demonstrates the strict order of arguments:
    1. Standard formal arguments
    2. *args
    3. **kwargs
    """
    print(f"Standard argument: {standard_arg}")
    print(f"args (packed as tuple)   : {args}")
    print(f"kwargs (packed as dict)  : {kwargs}")

# Example usage for combined arguments:
print("--- Testing Combined Arguments ---")
master_function("Hello", 1, 2, 3, status="Active", mode="Dark")
# Output:
# Standard argument: Hello
# args (packed as tuple)   : (1, 2, 3)
# kwargs (packed as dict)  : {'status': 'Active', 'mode': 'Dark'}