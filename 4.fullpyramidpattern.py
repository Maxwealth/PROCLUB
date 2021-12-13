a = 5

b = a - 1
for i in range(a):
    for j in range (b):
        print(end = " ")
    b = b - 1
    for j in range(i+1):
        print("* ", end="")
    print()
