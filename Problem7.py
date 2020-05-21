def check_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for j in range(3, int(n ** (1 / 2)) + 1, 2):
        if n % j == 0:
            return False
    return True


i = 0
n = 10001
ans = 2
while i < n:
    if check_prime(ans):
        i += 1
    ans += 1
print(ans-1)
