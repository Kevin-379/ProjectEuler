# By sieve of Eratosthenes
NUM = 2000000
is_prime = [True]*(NUM-1)
i = 0
ans = 0
while i < NUM-1:
    if is_prime[i]:
        for j in range(2*i+2, NUM-1, i+2):
            is_prime[j] = False
        ans += i+2
    i += 1
print(ans)
