#new class
from app.calculator import Calculator
def main():

        # Create an object of the Calculator class
        calculator = Calculator(5, 2)

        # Example usage of calculator methods
        print("Addition:", calculator.add())
        print("Subtraction:", calculator.subtract())
        print("Multiplication:", calculator.multiply())
        print("Division:", calculator.divide())
        print("Power:", calculator.power())
        print("Random Number (between 1 and 10):", Calculator.random_number(1, 10))

if __name__ == "__main__":
    main()


