def angka_sekali(a) :
    b = list()
    for c in set(a):
        if list(a).count(c) == 1:
            b.append(c)
    return b

angka = input()
print(sorted(angka_sekali(angka),reverse=True))
