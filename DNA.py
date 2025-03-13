# Rosalind Challenge - Counting DNA Nucleotides
# Given: a string "s" of length at most 1000nt
# Return: 4 integers separated by spaces
# counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

# First, visit Rosalind <https://rosalind.info/problems/dna/>
# Second, click blue button "Download Dataset" at bottom of page

# Open and read dataset.
with open('/Users/celinewest/Downloads/rosalind_dna.txt', 'r') as file: #Use your own directory with downloaded dataset
    DNA = file.read().strip()  # Remove extra spaces or new lines

# Initialize nucleotide counts
counts = {"A": 0, "C": 0, "G": 0, "T": 0}

# Count nucleotides
for letter in DNA:
    if letter in counts:
        counts[letter] += 1

# Print output in required order
print(counts["A"], counts["C"], counts["G"], counts["T"])

# Paste your output into Rosalind to solve the problem!