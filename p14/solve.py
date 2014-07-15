def count_cyclen(n):
    cnt = 0
    
    if(n == 1):
        return 1
    
    if(n%2 == 0):
        return 1+count_cyclen(n/2)
    else:
        return 1+count_cyclen(3*n+1)

max_cyclen = -1
max_i = -1

for i in xrange(1,1000001):
    cyclen_i = count_cyclen(i)
    if(cyclen_i > max_cyclen):
        max_cyclen = cyclen_i
        max_i = i

print max_i
