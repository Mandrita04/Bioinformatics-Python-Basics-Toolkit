#A bar plot showing frequency of each nucleotide in a DNA sequence
import matplotlib.pyplot as plt
from Bio import SeqIO

for record in SeqIO.parse("HPV16.fasta", "fasta"):
    dna = record.seq


# Count nucleotides
count = {
    'A': dna.count('A'),
    'T': dna.count('T'),
    'G': dna.count('G'),
    'C': dna.count('C')
}

# Print counts
print("\nNucleotide Counts")
for nucleotide, value in count.items():
    print(f"{nucleotide}: {value}")

# Plot bar chart
plt.figure(figsize=(6,4))
plt.bar(count.keys(), count.values())

plt.title("DNA Nucleotide Frequency")
plt.xlabel("Nucleotide")
plt.ylabel("Count")

plt.show()