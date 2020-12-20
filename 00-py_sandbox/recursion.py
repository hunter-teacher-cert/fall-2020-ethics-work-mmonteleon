# Clyde "Thluffy" Sinclair
# Aug 2020

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print("Good News Everyone!")
print(f"1! = {factorial(1)}" )
print(f"2! = {factorial(2)}" )
print(f"3! = {factorial(3)}" )
print(f"4! = {factorial(4)}" )
print(f"5! = {factorial(5)}" )

print(f"fib(1) = {fib(1)}" )
print(f"fib(2) = {fib(2)}" )
print(f"fib(3) = {fib(3)}" )
print(f"fib(4) = {fib(4)}" )
print(f"fib(5) = {fib(5)}" )
