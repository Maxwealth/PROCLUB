a = 5

b = 2*a - 2
for i in range(a):
    for j in range (b):
        print(end = " ")
    b = b - 2
    for j in range(i+1):
        print("* ", end="")
    print()
