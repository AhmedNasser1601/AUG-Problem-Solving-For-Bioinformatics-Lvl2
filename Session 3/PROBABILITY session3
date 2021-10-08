Created on Fri Oct  8 13:32:29 2021

@author: Mariam
"""
#flipping a coin
from scipy.stats import bernoulli
bernoulli.rvs(p=0.5, size=1)
#Flip 10 times 
bernoulli.rvs(p=0.5, size=10) #probability of sucess
#how many heads
sum(bernoulli.rvs(p=0.5, size=10))
#using binomial distribution
from scipy.stats import binom
binom.rvs(n=10, p=0.5, size=1)
# to make sure of the randomness we will run it again 
binom.rvs(n=10, p=0.5, size=4)
#-----------------------------------

# Probability of 2 heads after 10 throws with a fair coin
binom.pmf(k=2, n=10, p=0.5)
# Probability of 65 heads after 100 throws with p=0.7
binom.pmf(k=65, n=100, p=0.7)
# Probability of 5 heads or less after 10 throws with a fair coin
binom.cdf(k=5, n=10, p=0.5)
# Probability of more than 59 heads after 100 throws with p=0.7
1-binom.cdf(k=59, n=100, p=0.7)
binom.sf(k=59, n=100, p=0.7)
#--------------------------------------------------------------------------------------------------
#to find the permutation from 1
from itertools import permutations
le = list(permutations(range(1, 4)))
len(le)
print (le)


#--------------------------------------------------------------------------------------------------

# A Python program to print all
# permutations using library function
from itertools import permutations
 
# Get all permutations of [1, 2, 3]
perm = permutations([1, 2, 3])
 
# Print the obtained permutations
for i in list(perm):
    print (i)
    
    
  # A Python program to print all
# permutations of given length
from itertools import permutations
 
# Get all permutations of length 2
# and length 2
perm = permutations([1, 3, 2])
 
# Print the obtained permutations
for i in list(perm):
    print (i)  
    

#-----------------------------------------------------------------------------------------------------
# A Python program to print all
# combinations of given length
from itertools import combinations
 
# Get all combinations of [1, 2, 3]
# and length 2
comb = combinations([1, 2, 3], 2)
 
# Print the obtained combinations
for i in list(comb):
    print (i)
   
 # if the input list is sorted, the combination tuples will be produced in sorted order. 
 
 
# A Python program to print all combinations
# with an element-to-itself combination is
# also included
from itertools import combinations_with_replacement
 
# Get all combinations of [1, 2, 3] and length 2
comb = combinations_with_replacement([1, 2, 3], 2)
 
# Print the obtained combinations
for i in list(comb):
    print (i)
