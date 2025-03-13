# Rosalind challenge "Mendel's First Law"
# Given positive integers k, m, and n:
# representing a population containing k+m+n organisms
# k - homozygous dominant AA
# m - heterozygous Aa
# n - homozygous recessive aa

# Return the probability that two randomly selected mating organisms
# will produce an individual possessing a dominant allele (and thus a dominant phenotype)
# Assume that any two organisms can mate.

# P(dominant) = total dominant outcomes / total possible pairings

def dominant_allele_probability(k, m, n):
    # Total number of individuals
    total_population = k + m + n

    # Total pairings: (total_population choose 2)
    total_pairings = (total_population * (total_population - 1)) // 2 #combination formula - how many ways can 2 mates be chosen?

    # Dominant offspring outcomes:
    dominant_outcomes = 0

    # AA x AA pairs: probability = 1
    dominant_outcomes += (k * (k - 1)) // 2 * 1  # k choose 2 number of ways to choose 2 individuals * probability that offspring have a dominant allele.

    # AA x Aa pairs: probability = 1
    dominant_outcomes += k * m * 1

    # AA x aa pairs: probability = 1
    dominant_outcomes += k * n * 1  #

    # Aa x Aa pairs: probability = 0.75
    dominant_outcomes += (m * (m - 1)) // 2 * 0.75

    # Aa x aa pairs: probability = 0.5
    dominant_outcomes += m * n * 0.5

    # aa x aa pairs: probability = 0
    # no need to add to dominant_outcomes since probability is 0

    # Calculate probability of dominant offspring
    p_d = dominant_outcomes / total_pairings

    return p_d

print(round(dominant_allele_probability(20,27,24,),5))
