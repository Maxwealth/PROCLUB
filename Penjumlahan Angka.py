def penjumlahan_angka(numbers, target):
    temp = list()
    for a in numbers:
        for b in numbers:
            if (a+b) == target:
                temp.extend([numbers.index(a), numbers.index(b)])
                return temp
    return []


z = [int(x) for x in input().split()]
y = int(input())
print(penjumlahan_angka(z,y))
