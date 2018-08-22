def add(a, b):
    return a + b

while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(str(a) + ' + ' + str(b) + ' = ' + str(add(a, b)))
    print()
