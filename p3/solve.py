import math

num = 600851475143

def find_largest_prime_factor(n):
    max_fac = -1
    recurred = False
    for i in reversed(xrange(2, int(math.floor(math.sqrt(n))))):
        if(n%i == 0):
            recurred = True
            curmax = find_largest_prime_factor(i)
            if(curmax > max_fac):
                max_fac = curmax
    if(recurred == False):
        return n
    return max_fac

print find_largest_prime_factor(num)
