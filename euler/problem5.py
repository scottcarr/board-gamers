import reuseable as ru

def check_divisible(quo,div):

	for i in range(1,div):
		if quo%i != 0:
			return False
	return True

def find_not_divisible(quo,div):
	
	list=[]
	for i in range(1,div):
		if quo%i != 0:
			list.append(i)
	return list
	
def find_repeated_primes(num,n):
	#some of the prime factors must be repeated
	list = find_not_divisible(num,n)
	print list
	for item in list:
		for prime in primes:
			if item%prime==0:
				num *= prime
				if check_divisible(num,n):
					return num
					
	
n = 20

primes = ru.find_prime_factors(n)

print primes

num = 1

for prime in primes:
	num *= prime

print num
if ~check_divisible(num,n):
	print find_repeated_primes(num,n)
		