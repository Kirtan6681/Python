a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = input("Enter operation (+, -, *, /): ")

if c == '+':
    print("Result:", a + b)
elif c == '-':
    print("Result:", a - b)
elif c == '*':
    print("Result:", a * b)
elif c == '/':
    if b == 0:
        print("Cannot divide by zero.")
    else:
        print("Result:", a / b)
else:   
    print("Invalid operation.")
