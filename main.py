def fibonacci(n, sonuc=[]):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
        sonuc.append(str(a))
    return sonuc

sayi = int(input("Fiboncacci sayısının uzunluğu: "))

print("Cevap: {}".format(",".join(fibonacci(sayi))))
