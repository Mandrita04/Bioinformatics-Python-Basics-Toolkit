#Resctriction enzyme site finder
from Bio import SeqIO
for record in SeqIO.parse("HPV16.fasta","fasta"):
 seq=record.seq
for i in range(len(seq)):
    if seq[i:i+6]=="GAATTC":
        print("EcoRI site found at position:", i)
    elif seq[i:i+6]=="GGATCC":
        print("BamHI site found at position:", i)
    elif seq[i:i+6]=="AAGCTT":
        print("HindIII site found at position:", i)