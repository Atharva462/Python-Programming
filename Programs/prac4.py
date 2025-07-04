# Define custom exceptions
class CustomValueError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class CustomTypeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def exception_handling_demo(value):
    try:
        # Example of handling ValueError
        if value < 0:
            raise ValueError("Value cannot be negative.")
        
        # Example of handling TypeError
        if not isinstance(value, int):
            raise TypeError("Value must be an integer.")
        
        # Example of handling FileNotFoundError
        try:
            with open('non_existent_file.txt', 'r') as file:
                content = file.read()
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")
        
        # Example of raising and handling a custom exception
        if value == 10:
            raise CustomValueError("CustomValueError: Value cannot be 10.")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except TypeError as te:
        print(f"TypeError: {te}")
    except CustomValueError as cve:
        print(f"CustomValueError: {cve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
print("Testing with a negative value:")
exception_handling_demo(-5)

print("\nTesting with a non-integer value:")
exception_handling_demo('string')

print("\nTesting with a valid value that causes FileNotFoundError:")
exception_handling_demo(5)

print("\nTesting with a value that triggers CustomValueError:")
exception_handling_demo(10)

print("\nTesting with a valid value that does not cause any exceptions:")
exception_handling_demo(3)
