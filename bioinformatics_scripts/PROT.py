# Rosalind challenge "Translating RNA into Protein"
# Given an mRNA string, return the corresponding protein string

# Read file
with open('/Users/celinewest/Downloads/rosalind_prot-2.txt', 'r') as file:
    rna_sequence = file.read().strip() #removes extra spaces or new lines

# Iterate over the string in steps of 3
for i in range(0, len(rna_sequence), 3):
    codon = rna_sequence[i:i+3]  # Get the current 3-character substring
    print(codon)  # This will print each codon

# Store info about each codon in a dictionary
codon_table = {
    "UUU": "F", "UUC": "F",  # Phenylalanine
    "UUA": "L", "UUG": "L",  # Leucine
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",  # Leucine
    "AUU": "I", "AUC": "I", "AUA": "I",  # Isoleucine
    "AUG": "M",  # Methionine (Start codon)
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",  # Valine
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",  # Serine
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",  # Proline
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",  # Threonine
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",  # Alanine
    "UAU": "Y", "UAC": "Y",  # Tyrosine
    "UAA": "Stop", "UAG": "Stop", "UGA": "Stop",  # Stop codons
    "CAU": "H", "CAC": "H",  # Histidine
    "CAA": "Q", "CAG": "Q",  # Glutamine
    "AAU": "N", "AAC": "N",  # Asparagine
    "AAA": "K", "AAG": "K",  # Lysine
    "GAU": "D", "GAC": "D",  # Aspartic acid
    "GAA": "E", "GAG": "E",  # Glutamic acid
    "UGU": "C", "UGC": "C",  # Cysteine
    "UGG": "W",  # Tryptophan
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",  # Arginine
    "AGU": "S", "AGC": "S",  # Serine
    "AGA": "R", "AGG": "R",  # Arginine
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"   # Glycine
}

# Empty list to store protein sequence
protein = []

# Iterate over RNA sequence 3 nucleotides or 1 codon at a time
for i in range(0, len(rna_sequence), 3):
    codon = rna_sequence[i:i + 3]  # Get the current codon
    amino_acid = codon_table.get(codon)  # Lookup the amino acid for this codon

    if amino_acid == "Stop":
        break  # Stop translation if a stop codon is found

    if amino_acid:  # Ensure that the codon is valid (not None)
        protein.append(amino_acid)

# Join the protein list into a single string to represent the full protein
protein_sequence = ''.join(protein)
print(protein_sequence)

# Create a .txt file to write output
with open('protein_output-1.txt', 'w') as file: #Use your own directory with downloaded dataset
    file.write(protein_sequence)