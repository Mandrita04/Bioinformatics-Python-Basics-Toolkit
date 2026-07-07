#Reverse complement of DNA sequence
from Bio import SeqIO
for record in SeqIO.parse("HPV16.fasta", "fasta"):
    seq=record.seq
    rev=seq.reverse_complement()
    print("Original sequence:", seq)
    print("Correct direction:", rev[::-1])
    print("Reverse complement:", rev)