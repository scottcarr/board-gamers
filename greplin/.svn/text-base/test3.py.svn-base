import csv
import pdb
import itertools

def return_subsets(set,i):
    
    matches=[]
    n_matches=0
    for n in range(i):
        subsets = itertools.combinations(set[:i],n)
        for subset in subsets:
            if sum(subset) == set[i]:
                complete_set=[]
                for item in subset:
                    complete_set.append(item)
                complete_set.append(set[i])
                matches.append(complete_set)
                n_matches+=1
    return n_matches
            
    
    

reader = csv.reader(open('numbers.csv','r'))

input = reader.next()

set=[]
for item in input:
    set.append(int(item))

print set

total_matches = 0
for i in range(len(set)):
    if i != 0:
        total_matches += return_subsets(set,i)
        
print total_matches    

