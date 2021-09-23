def recur_fib(n):
    if n <= 1:
        return n
    else:
        return recur_fib(n-1) + recur_fib(n-2)


num = int(input('Input number: '))
ans = recur_fib(num)
print(ans)
'''

'''
def dp_fib(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]


num = int(input('Input number: '))
ans = dp_fib(num)
print(ans)
