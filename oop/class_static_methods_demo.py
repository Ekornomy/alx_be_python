class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static Method - add(a, b): Returns the sum of two numbers.
        Uses the @staticmethod decorator.
        Doesn't need access to class or instance attributes.
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class Method - multiply(cls, a, b): Returns the product of two numbers.
        Uses the @classmethod decorator and prints the class attribute calculation_type.
        The cls parameter gives access to class-level attributes and methods.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b