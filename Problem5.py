def check_prime(n):
    if n%2 == 0 and n != 2:
        return False
    for j in range(3, int(n**(1/2))+1, 2):
        if n%j == 0:
            return False
    return True


def div(n):
    ans = 1
    for i in range(2, n):
        if check_prime(i):
            p = i
            while p < n:
                p *= i
            ans *= p//i
    return ans


print(div(20))
