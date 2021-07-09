s = 0
digits = [str(i) for i in range(1, 10)]
answers = set()
for i in range(100, 1000):
    for j in range(10, 100):
        if i * j < 10000:
            digits_0 = digits[:]
            flag = True
            string = str(i) + str(j) + str(i * j)
            for k in string:
                if k in digits_0:
                    digits_0.remove(k)
                else:
                    flag = False
                    break
            if flag:
                answers.add(i*j)
                print(i,"*",j,'=',i*j)

for i in range(1, 10):
    for j in range(1000, 10000):
        if i * j < 10000:
            digits_0 = digits[:]
            flag = True
            string = str(i) + str(j) + str(i * j)
            for k in string:
                if k in digits_0:
                    digits_0.remove(k)
                else:
                    flag = False
                    break
            if flag:
                answers.add(i * j)
                print(i, "*", j, '=', i * j)
print((answers))