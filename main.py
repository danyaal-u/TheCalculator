# The Calculator for a 2 number calculation

print("Welcome to danyaal's amazing calculator! <3")
first = input("First: ")
second = input("Second: ")
operation = input("What operation, *, +, /, -")
if operation == "+":
    answer = int(first) + int(second)
    print(answer)
elif operation == "-":
    answer = int(first) - int(second)
    print(answer)
elif operation == "/":
    answer = int(first) / int(second)
    print(answer)
elif operation == "*":
    answer = int(first) * int(second)
    print(answer)
