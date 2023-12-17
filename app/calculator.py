# app/calculator.py
import math
import random

class Calculator:
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def add(self):
        return self.operand1 + self.operand2

    def subtract(self):
        return self.operand1 - self.operand2

    def multiply(self):
        return self.operand1 * self.operand2

    def divide(self):
        if self.operand2 != 0:
            return self.operand1 / self.operand2
        else:
            return "Cannot divide by zero."

    def power(self):
        return math.pow(self.operand1, self.operand2)

    @staticmethod
    def random_number(a, b):
        return random.uniform(a, b)

