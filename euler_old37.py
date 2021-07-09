from sieve_of_eratosthenes import sieve_1 as sv


def nice_property(n):
    n = str(n)
    length = len(n)
    if length == 1:
        return False
    else:
        for i in range(1, length):
            if (int(n[i:]) not in prime) or (int(n[:-i]) not in prime):
                return False
        return True


prime = sv(10 ** 6)
odd_numbers = (i for i in range(0, 10, 2))
print(odd_numbers)
s = 0
counter = 0
while counter != 11:
    for number in prime:
        if nice_property(number):
            counter += 1
            s += number
print(s)
