#Homopolymer strength calculation
from Bio import SeqIO

record = SeqIO.read("HPV16.fasta", "fasta")

sequence = str(record.seq)

max_base = ""
max_length = 0

current_base = sequence[0]
current_length = 1

for i in range(1, len(sequence)):
    if sequence[i] == current_base:
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
            max_base = current_base

        current_base = sequence[i]
        current_length = 1

if current_length > max_length:
    max_length = current_length
    max_base = current_base

print("Longest Homopolymer:", max_base * max_length)
print("Length:", max_length)