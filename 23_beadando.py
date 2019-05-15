import time
import math
from itertools import count

print("huszonharmadik feladat")


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def getprimes(n):
    primes = [2]
    for i in count():
        if is_prime(i):
            primes.append(i)
        if len(primes) == n:
            return primes[-1]


t0 = time.time()
print(getprimes(10000))
t1 = time.time()
print("A program futásának ideje:", t1 - t0)
