def sumsqdiff_loop(n):
    ans = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            ans += i*j
    return 2*ans


def sumsqdiff_formula(n):
    sqsum = (n*(n+1)//2)**2
    sumsq = (n*(n+1)*(2*n+1))//6
    return sqsum - sumsq


print(sumsqdiff_loop(100))
print(sumsqdiff_formula(100))
