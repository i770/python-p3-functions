#!/usr/bin/env python3

from functions import greet_programmer, greet, greet_with_default, \
                        add, halve

import io
import sys


class TestGreetProgrammer:
    '''function greet_programmer()'''

    def greet_programmer():
        print("Hello, programmer!")
        
class TestGreet:
    '''function greet()'''

    def greet_programmer():
        print("Hello, prgrammer!")
        
class TestGreetWithDefault:
    '''function greet_with_default()'''

    def test_greet_with_default(self):
         print("Hello, programmer!")
        
    def test_greet_with_default_with_param(self):
         print("Hello, Guido!")
        
class TestAdd:
    '''function add()'''

    def test_add(self):
    
        add(45, 55)

class TestHalve:
    '''function halve()'''

    def test_halve_int(self):
       
        halve(100) 

    def test_halve_float(self):
      
        halve(99.0)
