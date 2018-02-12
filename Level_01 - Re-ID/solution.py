from math import sqrt; from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def gen_primes(upperbound):
    num = 2
    l = ''

    while len(l) < upperbound:
        if(is_prime(num)):
            l += str(num)
        num += 1
    return l

def answer(n):
    prime_string = gen_primes(10005)
    end = n + 5
    return prime_string[n:end]
