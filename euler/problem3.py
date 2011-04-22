import reuseable as ru

def find_prime_divisors(n):
    prime_divisors=[]
    #myrange = range(round(n/2)) #integer prime factors must be greater than or equal to n/2?
    for m in range(1,100000):
        if n%m==0:
            if ru.check_prime(m):
                prime_divisors.append(m)
                print prime_divisors
                product = 1
                for item in prime_divisors:
                    product *= item
                if product==n:
                    return prime_divisors
    return None
                
                
    

n = 600851475143
#n = 13195

p_d_list = find_prime_divisors(n)

print max(p_d_list)
