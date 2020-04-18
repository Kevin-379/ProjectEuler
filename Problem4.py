def palindrome():
    ans = 0
    for i in reversed(range(110, 1000, 11)):
        for j in reversed(range(100, 1000)):
            product = i*j
            if str(product) == str(product)[::-1]:
                if product > ans:
                    ans = product
    return ans


print(palindrome())
