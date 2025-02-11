# lib/functions.py

def greet_programmer():
    """
    Prints "Hello, programmer!" to the terminal.
    """
    print("Hello, programmer!")

def greet(name):
    """
    Prints "Hello, name!" to the terminal, where `name` is the argument passed.
    """
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    """
    Prints "Hello, name!" to the terminal, where `name` is the argument passed.
    If no argument is passed, it defaults to "programmer".
    """
    print(f"Hello, {name}!")

def add(num1, num2):
    """
    Takes two numbers as arguments and returns their sum.
    """
    return num1 + num2

def halve(number):
    """
    Takes a number as an argument and returns its value divided by two.
    """
    return number / 2