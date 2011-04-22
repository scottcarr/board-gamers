def check_prime(n):
    if n==1:
        return False
    elif n==2:
        return True
    else:
            m = range(n)
            #pdb.set_trace()
            i=2
            if n%2==0:
                return False
            else:
                while m[i]*m[i] <= n:
                    if n%m[i] == 0:
                        return False
                    i+=1
                return True
            
def find_prime_factors(n):
    primes=[]
    for i in range(n):
        if check_prime(i):
            primes.append(i)
    return primes