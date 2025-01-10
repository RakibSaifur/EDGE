#pattern 2
i = 1
j = 1
while i<=5:
    spaces = (5 - i) * 2
    print(' ' *spaces,end=' ')
    j=1
    while j<=i:
        print(j,end=' ')
        j += 1
    print()
    i += 1