# Rosalind Challenge Rabbits and Recurrence Relations
# Given positive integers n≤40 and k≤5
# Return The total number of rabbit pairs that will be present after n months,
# if we begin with 1 pair and in each generation,
# every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

# Assumptions about the population:
# 1. The population begins in the first month with a pair of newborn rabbits.
# 2. Rabbits reach reproductive age after one month.
# 3. In any given month, every rabbit of reproductive age mates with another rabbit of reproductive age.
# 4. Exactly one month after two rabbits mate, they produce one male and one female rabbit.
# 5. Rabbits never die or stop reproducing.

import numpy as np

F = np.zeros(32)
# F[0] = 1
# F[1] = 1
# grown (2-1) + k_babies (2-2)

for n in range(0, 32):
    if n == 0 or n == 1: # base case
        F[n] = 1
    else:
        F[n] = F[n-1] + 3*F[n-2] # recurrence relation
print(F.astype(int))
print(F[-1].astype(int))