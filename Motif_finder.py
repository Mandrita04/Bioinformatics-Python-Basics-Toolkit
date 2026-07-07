#Motif finding and recording its occurance
from Bio import SeqIO

record = SeqIO.read("HPV16.fasta", "fasta")

sequence = str(record.seq)

motif = "AGC"

positions = []

for i in range(len(sequence) - len(motif) + 1):
    if sequence[i:i+len(motif)] == motif:
        positions.append(i + 1)

print("Positions:", positions)
print("Occurrences:", len(positions))