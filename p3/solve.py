import math

def find_largest_prime_factor(n):
    max_fac = -1
    for i in reversed(xrange(2, int(math.floor(math.sqrt(n))))):
        if(n%i == 0):
            curmax = find_largest_prime_factor(i)
            if(curmax > max_fac):
                max_fac = curmax
    if(max_fac == -1):
        return n
    return max_fac

num = 600851475143
print find_largest_prime_factor(num)
