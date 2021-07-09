numbers = []
for i in range(10):
    print(i)
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for f in range(10):
                    for q in range(10):
                        for w in range(10):
                            s = i * 1000000 + j * 100000 + k * 10000 + l * 1000 + f * 100 + q * 10 + w
                            if s == i ** 5 + j ** 5 + k ** 5 + l ** 5 + f ** 5 + q ** 5 + w ** 5:
                                numbers.append(s)
print((numbers))
