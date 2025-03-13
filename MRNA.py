# Rosalind problem "Inferring mRNA from Protein"
# Given a protein string of at most 1000 aa
# Return the total number of different RNA strings from which the protein could have been translated, modulo 1,000,000
# (Don't neglect the importance of the stop codon in protein translation.)

aa_codons = {
    "F": ["UUU", "UUC"],
    "L": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
    "I": ["AUU", "AUC", "AUA"],
    "M": ["AUG"],
    "V": ["GUU", "GUC", "GUA", "GUG"],
    "S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
    "P": ["CCU", "CCC", "CCA", "CCG"],
    "T": ["ACU", "ACC", "ACA", "ACG"],
    "A": ["GCU", "GCC", "GCA", "GCG"],
    "Y": ["UAU", "UAC"],
    "Stop": ["UAA", "UAG", "UGA"],
    "H": ["CAU", "CAC"],
    "Q": ["CAA", "CAG"],
    "N": ["AAU", "AAC"],
    "K": ["AAA", "AAG"],
    "D": ["GAU", "GAC"],
    "E": ["GAA", "GAG"],
    "C": ["UGU", "UGC"],
    "W": ["UGG"],
    "R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "G": ["GGU", "GGC", "GGA", "GGG"]
}

def different_RNA_strings_mod(protein_seq):
    different_RNA_strings = 3 # Multiply everything by 3 to include the Stop codon
    for aa in protein_seq:
        codons = aa_codons[aa]
        different_RNA_strings = different_RNA_strings * len(codons) % int(1e6)
    return different_RNA_strings

# read .txt file
with open('/Users/celinewest/Downloads/rosalind_mrna-7.txt', 'r') as file: #Use your own directory with downloaded dataset
    protein_seq = file.read().strip() #removes extra spaces or new lines
total_sequences = different_RNA_strings_mod(protein_seq)
print(total_sequences)