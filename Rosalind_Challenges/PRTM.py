# Rosalind Challenge - Calculating Protein Mass
# Given: A protein string P of length at most 1000 aa.
# Return: The total weight of P. Consult the monoisotopic mass table.

# Monoisotopic mass table
mass_dictionary = { "A": 71.03711,
               "C": 103.00919,
               "D": 115.02694,
               "E": 129.04259,
               "F": 147.06841,
               "G": 57.02146,
               "H": 137.05891,
               "I": 113.08406,
               "K": 128.09496,
               "L": 113.08406,
               "M": 131.04049,
               "N": 114.04293,
               "P": 97.05276,
               "Q": 128.05858,
               "R": 156.10111,
               "S": 87.03203,
               "T": 101.04768,
               "V": 99.06841,
               "W": 186.07931,
               "Y": 163.06333}

# Empty string to store the total weight of P.
total_mass = 0

# Open and read dataset.
with open('/Users/celinewest/Downloads/rosalind_prtm-2.txt', 'r') as file: #Use your own directory with downloaded dataset
    p = file.read().strip()  # Remove extra spaces or new lines

print(p)

# Count nucleotides
for protein in p:
   total_mass += mass_dictionary[protein]

print(total_mass)

