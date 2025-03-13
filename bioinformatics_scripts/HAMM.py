# Rosalind.info problem "Counting Point Mutations"
# Problem: given two strings of an equal length, find the Hamming distance between s and t

# Open the file and read the lines
with open('/Users/celinewest/Downloads/rosalind_hamm-3.txt', 'r') as file: #Use your own directory with downloaded dataset
    # Read the first line and remove any extra whitespace/newline characters
    strand1 = file.readline().strip()

    # Read the second line and remove any extra whitespace/newline characters
    strand2 = file.readline().strip()

# Print the cleaned strings
print("Strand 1:", strand1)
print("Strand 2:", strand2)


def hamming_distance(strand1, strand2):

# Ensure strings are the same length
    if len(strand1) != len(strand2):
     raise ValueError("Strings must be the same length!")

# Compare each character in the string and count differences
# The zip function combines two sequences into pairs of elements (first character of strand1 with first character of strand2)
# The for loop iterates over the pairs made by zip. c1 and c2 are characters of each string
# The characters are compared to see if they're the same.
# Sum adds up all true values from the comparison
    return sum(c1 != c2 for c1, c2 in zip(strand1, strand2))

print(hamming_distance(strand1,strand2))
