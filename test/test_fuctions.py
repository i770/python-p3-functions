# tests/test_functions.py

from lib.functions import greet_programmer, greet, greet_with_default, add, halve

def test_greet_programmer():
    # Test that greet_programmer() prints "Hello, programmer!"
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    greet_programmer()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == "Hello, programmer!"

def test_greet():
    # Test that greet("Alice") prints "Hello, Alice!"
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    greet("Alice")
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == "Hello, Alice!"

def test_greet_with_default():
    # Test that greet_with_default() prints "Hello, programmer!"
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    greet_with_default()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == "Hello, programmer!"

    # Test that greet_with_default("Bob") prints "Hello, Bob!"
    captured_output = io.StringIO()
    sys.stdout = captured_output
    greet_with_default("Bob")
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == "Hello, Bob!"

def test_add():
    # Test that add(3, 5) returns 8
    assert add(3, 5) == 8

def test_halve():
    # Test that halve(10) returns 5.0
    assert halve(10) == 5.0