import math

def ncr(n, r):
    return (math.factorial(n) // (math.factorial(r) * math.factorial(n-r)))

def prob(k, x): #Offsprings having AaBb
    return (ncr(2**k, x) * (0.25**x) * (0.75**(2**k - x)))


file = open("rosalind_lia.txt", "r")
params = file.readline().split(' ')

k = int(params[0])
n = int(params[1])

total = 0.0
file.close()

for i in range(n): #from 0 to n-1
    total += prob(k, i)

print(round(1 - total, 3))


#Explaination
'''
    Probability of [(Aa offspring) and (unknown parent)] is = 0.5 (AA, Aa, aa)
    Probability of [(Bb offspring) and (unknown parent)] is = 0.5 (BB, Bb, bb)
    Probability of [(AaBb offspring) together] is = (0.5 * 0.5) = 0.25

    The probability that EXACTLY (X) individuals will have (AaBb out of 2^k total)
        is = nCr(2^k, x) * 0.25^x * (1-0.25)^(2^k - x)

    Use the complement rule for (AaBb) = 1 - (Pr(0) + Pr(1) +...+ Pr(n-1))
'''