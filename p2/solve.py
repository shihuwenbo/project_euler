seq = [0,1]

i = 1
while(True):
    next = seq[i-1]+seq[i]
    seq.append(next)
    i += 1
    if(next > 4000000):
        break

total = 0
for i in xrange(2, len(seq)):
    if(seq[i]%2 == 0):
        total += seq[i]

print total
