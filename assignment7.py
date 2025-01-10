# GCD
a = int(input("Enter first number"))
b = int(input("Enter second number"))
if a < 0:
    a = -a
if b < 0:
    b = -b
while b:
    a, b = b, a % b
print("GCD is:", a)
