#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 10):
        if i & 15 != 0 or i % 3 != 0 or i & 5 != 0:
            print(f"{i:d}", end=" ")
        elif i & 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
