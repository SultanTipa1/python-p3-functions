#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()

def greet(name):
    print(f"Hello, {name}!")

greet("Naureen!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("Sunny")

def add(num1, num2):
    print(f" {num1} + {num2} = {num1 + num2}")

add(1, 2)

def halve(number):
    print(f"{number} /2 = {number / 2}")

    return number/2

halve(4)

def add(num1, num2):
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
    return result

add(45, 55)