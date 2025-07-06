class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        # Correct implementation
        return a * b

    def divide(self, a, b):
        # Missing division by zero check (code smell)
        return a / b

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("Add 5 + 3:", calc.add(5, 3))
    print("Multiply 5 * 3:", calc.multiply(5, 3))
    print("Divide 10 / 2:", calc.divide(10, 2))
