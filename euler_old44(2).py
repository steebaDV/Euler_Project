amount = 4
n = 10**6
numbers = [0]*n
counter = 0
for i in range(n):
    if i < 2:
        continue
    elif numbers[i] == 0:
        for j in range(i, n, i):
            numbers[j]+=1
        counter = 0
    elif numbers[i] == amount:
        counter += 1
        if counter == amount:
            break
    else:
        counter = 0
print(i - amount + 1)