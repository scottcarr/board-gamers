import pdb

def find_prime_divisors(n):
	m = range(n)
	
	divisors = []
	for num in m:
		if num != 0:
			if n%num==0:
				divisors.append(num)
	
	primes=[]
	for num in divisors:
	   if check_prime(num):
	   	   primes.append(num)
	

	print primes    
	return sum(primes)
	   
	 

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
                while m[i]*m[i] < n:
                    if n%m[i] == 0:
                        return False
                    i+=1
                return True

def find_next_fib(seq):
    seq.append(seq[-1]+seq[-2])
    return seq
            
min = 217000
#min = 13

fib=[0,1,1]


while fib[-1] < min:
    fib.append(fib[-1]+fib[-2])
        
#print fib

not_done = True

#pdb.set_trace()

while not_done:
    if check_prime(fib[-1]):
        not_done = False
    else:
        fib = find_next_fib(fib)

print fib[-1]
    
x = fib[-1]+1

print find_prime_divisors(x)