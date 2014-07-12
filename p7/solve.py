import math

def is_prime(n):
    for i in xrange(2, int(math.floor(math.sqrt(n))+1)):
        if(n%i == 0):
            return False
    return True

i = 2
j = 0
while(True):
    if(is_prime(i)):
        j += 1
    if(j == 10001):
        break
    i += 1

print i
