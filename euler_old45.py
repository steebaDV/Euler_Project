def pent(k):
    di = 1 + 24 * k
    sqrt = di ** 0.5
    if int(sqrt) == sqrt:
        if (1 + sqrt) / 6 == int((1 + sqrt) / 6):
            return True
        else:
            return False
    else:
        return False


def trin(k):
    di = 1 + 8 * k
    sqrt = di ** 0.5
    if int(sqrt) == sqrt:
        if (-1 + sqrt) / 2 == int((-1 + sqrt) / 2):
            return True
        else:
            return False
    else:
        return False


for i in range(1, 10**9):
    n = i * (2 * i - 1)
    if pent(n) and trin(n):
        print(n)