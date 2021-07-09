from sieve_of_eratosthenes import sieve_2 as sv


def wow(digits, n):
    a = list(range(n))
    b = []
    b.append(a[:])
    point = -1
    now = point
    while True:
        flag = True
        for i in range(-n, 0):
            if a[i] == digits + i:
                point = i - 1
                flag = False
                break
        if point == -(n + 1):
            break
        if flag:
            point = -1
        a[point] += 1
        if now != point:
            now = point
            for i in range(point + 1, 0):
                a[i] = a[point] + i - point
        b.append(a[:])
    return b


n = 4
prime_0 = sv(10 ** 7)
print('wow')
prime = [i for i in prime_0 if i != 0 and i < 10 ** 3]
length = len(prime)
pairs = {}
for i in range(length - 1):
    i_pr = prime[i]
    for j in range(i + 1, length):
        j_pr = prime[j]
        if (prime_0[int(str(j_pr) + str(i_pr))] != 0) and (
                prime_0[int(str(i_pr) + str(j_pr))] != 0):
            try:
                pairs[i_pr].append(j_pr)
            except KeyError:
                pairs[i_pr] = []
                pairs[i_pr].append(j_pr)
s = 9999999
for keys, values in pairs.items():
    length = len(values)
    massive = wow(length, 3)
    for i in massive:
        try:
            og = set(values) & set(pairs[values[i[1]]]) & set(pairs[values[i[0]]]) & set(pairs[values[i[2]]])
        except KeyError:
            continue
        if og:
            print(keys, values[i[0]], values[i[1]], values[i[2]],og)
            for j in og:
                print(keys + values[i[0]] + values[i[1]] + values[i[2]] + j)
