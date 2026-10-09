"""
CODSOFT Python Programming Internship
Task 2: Calculator

Prompts the user for two numbers and an arithmetic operation,
then displays the result.
"""

def calculate(first_number, second_number, operation):
    """Perform a basic arithmetic operation and return the result."""
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number / second_number
    else:
        raise ValueError("Invalid operation. Choose +, -, * or /.")


def main():
    print("========== SIMPLE CALCULATOR ==========")
    print("Available operations: +  -  *  /")

    try:
        first_number = float(input("Enter the first number: "))
        operation = input("Choose an operation (+, -, *, /): ").strip()
        second_number = float(input("Enter the second number: "))

        result = calculate(first_number, second_number, operation)
        print(f"Result: {first_number:g} {operation} {second_number:g} = {result:g}")

    except ValueError as error:
        print(f"Input error: {error}")
    except ZeroDivisionError as error:
        print(f"Calculation error: {error}")


if __name__ == "__main__":
    main()
