def generate_fib(n):
    fib = [1,2,3]
    while fib[-1]<n:
        fib.append(fib[-2]+fib[-1])
    return fib[:-1]
        
max = 4*(10**6)

#print max

fib = generate_fib(max)

evens=[]
for num in fib:
    if num%2==0:
        evens.append(num)

print sum(evens)