a,b = 3,2
counter = 0
for i in range(999):
    a, b = 2*b + a, a + b
    if len(str(a)) > len(str(b)):
        counter += 1
print(counter)