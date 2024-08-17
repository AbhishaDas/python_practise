class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

# Example usage:
math_ops = MathOperations()
print("Sum (2 parameters):", math_ops.add(5, 3))
print("Sum (3 parameters):", math_ops.add(5, 3, 2))