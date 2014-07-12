import math

def is_prime(n):
    for i in xrange(2, int(math.floor(math.sqrt(n)))+1):
        if(n%i == 0):
            return False
    return True

i = 2
s = 0
while(True):
    if(is_prime(i)):
        s += i
    i += 1
    if(i > 2000000):
        break
print s
