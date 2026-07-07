#DNA nucleotide count
from Bio import SeqIO

for record in SeqIO.parse("HPV16.fasta", "fasta"):
    sequence =record.seq
    count = sequence.count("A") + sequence.count("T") + sequence.count("G") + sequence.count("C")#to count the number of ATCG
print("Total count of nucleotides:", count)
print("Count of A:",sequence.count("A") )
print("Count of T:",sequence.count("T") )
print("Count of G:",sequence.count("G") )
print("Count of C:",sequence.count("C") )