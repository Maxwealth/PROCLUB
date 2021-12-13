a = 4

b = 2*a - 2
for i in range(a, -1 , -1):
    for j in range (b, 0, -1):
        print(end = " ")
    b = b + 1
    for j in range(i+1):
        print("* ", end="")
    print()
