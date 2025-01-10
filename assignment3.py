#finding the prime numbers till n
n = int(input("enter a number"))
for i in range(2, n):
    for j in range(2, 101):
        if i%j == 0:
            break
    if i == j:
        print(i,end=",")