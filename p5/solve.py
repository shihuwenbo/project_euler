import math

def is_prime(n):
    for i in xrange(2, int(math.floor(math.sqrt(n)))+1):
        if(n%i == 0):
            return False
    return True

def prime_fact(n):
    fact = []
    for i in xrange(2, int(math.floor(math.sqrt(n)))+1):
        if(n%i == 0 and is_prime(i)):
            fact.append(i)
            fact += prime_fact(n/i)
            break
    if(len(fact) == 0):
        fact.append(n)
    return fact

def get_power(fact):
    powers = dict()
    for f in fact:
        if(f not in powers):
            powers[f] = 0
        powers[f] += 1
    return powers

all_fact_power = dict()
for i in xrange(1,21):
    all_fact_power[i] = get_power(prime_fact(i))

max_fact = dict()
for i in all_fact_power:
    for f in all_fact_power[i]:
        if(f not in max_fact):
            max_fact[f] = all_fact_power[i][f]
        if(all_fact_power[i][f] > max_fact[f]):
            max_fact[f] = all_fact_power[i][f]

prod = 1
for f in max_fact:
    prod = prod*math.pow(f, max_fact[f])

print int(prod)
