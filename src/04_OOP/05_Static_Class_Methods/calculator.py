from functools import reduce

class Calculator:

    @staticmethod
    def add(*args):
        """
        sums all the arguments passed to the function and returns the result
        :param args:
        :return: sums all the arguments
        """
        return reduce(lambda a, b: a + b, args)

    @staticmethod
    def multiply(*args):
        """
        multiplies all the numbers and returns the result
        :param args:
        :return:
        """
        return reduce(lambda a, b: a * b, args)

    @staticmethod
    def divide(*args):
        """
        divides all the numbers (starting from the first one) and returns the result
        :param args:
        :return:
        """
        return reduce(lambda a, b: a / b, args)

    @staticmethod
    def subtract(*args):
        """
        subtracts all the numbers (starting from the first one) and returns the result
        :param args:
        :return: subtracts all the numbers
        """
        return reduce(lambda a, b: a - b, args)

print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
