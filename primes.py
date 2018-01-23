##code a function "primes" which accepts an argument, "num", and returns the first num prime numbers in order

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
        else:
            return True

def primes(num):
    primes_list = []
    n = 1
    while len(primes_list) < (num):
        if is_prime(n) == True:
            primes_list.append(n)
        n += 1
    return primes_list
print(primes(10))
