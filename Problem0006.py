def sumsqdiff_loop(n):
    ans = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            ans += i*j
    return 2*ans


def sumsqdiff_formula(n):
    ans = n*(n**2-1)*(3*n+2)//12
    return ans


print(sumsqdiff_loop(100))
print(sumsqdiff_formula(100))
