def main():
    print("Welcome to my Python project!")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")

def add_numbers(a, b):
    return a + b

def example_function():
    return "This is an example function."

if __name__ == "__main__":
    main()