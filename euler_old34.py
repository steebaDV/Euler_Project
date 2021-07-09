import fact

factorization = [fact.fact(i) for i in range(10)]
summa = 0
i = 9
while True:
    i += 1
    s = 0
    counter = i
    while counter != 0:
        s += factorization[counter % 10]
        counter //= 10
    if s == i:
        print(i)
        summa +=i
        print(summa)
