def dp_fib(n, k):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + (f[i-2])*k)
    return f[n]


n = int(input('n: '))
k = int(input('k: '))
ans = dp_fib(n, k)
print(ans)
