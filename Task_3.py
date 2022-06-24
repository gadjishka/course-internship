def zeros(n):
    ans = 0
    while(n > 0):
        n /= 5
        ans += int(n)
    return ans


print(zeros(0))
print(zeros(6))
print(zeros(29))

