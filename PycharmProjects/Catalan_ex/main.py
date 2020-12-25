
from time import time
start = time()
# Using recursive programming


def catalan(n):
    if n <= 0:
        return 1
    else:
        s = 0
        for i in range(n):
            s += catalan(i)*catalan(n-1-i)
        return s


print(catalan(5))
end = time()
print(f'func 1 took {end - start} seconds!')


start1 = time()
# Using dynamic programming


def catal(n):
    t = [1]
    for i in range(1, n):
        newcat = 0
        for j in range(i):
            newcat += t[j]*t[i-j-1]
        t.append(newcat)
    return t[-1]


print(catal(6))
end1 = time()
print(f'func 2 took {end1 - start1} seconds!')
# Using the formula of catalan numbers


def factorial(a):
    if a == 0:
        return 1
    if a > 0:
        s = 1
        for i in range(1, a+1):
            s *= i
        return s
    else:
        return -1


start2 = time()


def bestcat(n):
    a = factorial(2*n)
    b = factorial(n)
    return int(a/(b*b*(n+1)))


print(bestcat(5))
end2 = time()
print(f'func 3 took {end2 - start2} seconds!')
