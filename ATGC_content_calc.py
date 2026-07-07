#ATGC Content calculator
from Bio import SeqIO

for record in SeqIO.parse("HPV16.fasta", "fasta"):
    sequence = record.seq
A = sequence.count("A")
T = sequence.count("T")
G = sequence.count("G")
C = sequence.count("C")

gc = ((G + C) / len(sequence)) * 100

print("Length:", len(sequence))
print("GC Content:", gc)
print("AT Content:",100-gc)