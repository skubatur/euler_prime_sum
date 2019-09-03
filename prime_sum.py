from bisect import bisect_left
T = int(input())

primes = [True for i in range(10**6+1)]

def get_primes():
    p = 2
    
    while p * p <= 10**6:
        if primes[p] == True:
            for i in range(2*p, 10**6+1, p):
                primes[i] = False
                
                
        p += 1
                
get_primes()
sum_ = {}

def get_sum():
    running_sum = 0
    
    for i in range(2, 10**6+1):
        if primes[i] == True:
            running_sum += i
            
        sum_[i] = running_sum
            
get_sum()

for _ in range(T):
    N = int(input())
    print(sum_[N])
