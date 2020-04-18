def check_prime(n):
    if n%2 == 0 and n != 2:
        return False
    for j in range(3, int(n**(1/2))+1, 2):
        if n%j == 0:
            return False
    return True


def f(n):
    prime_factors = set()
    i = 2
    while n > 1:
        if check_prime(i):
            if n%i == 0:
                n = n//i
                prime_factors.add(i)
                continue
        i += 1
    return prime_factors


print(f(600851475143))
