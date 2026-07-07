#Reading a fasta file
#Fasta file of HPV16 genome sequence
from Bio import SeqIO
for record in SeqIO.parse("HPV16.fasta", "fasta"):
    print("ID:", record.id)
    print("Sequence:", record.seq)