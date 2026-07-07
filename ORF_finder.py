#ORF finder
from Bio import SeqIO
for record in SeqIO.parse("HPV16.fasta","fasta"):
 dna=record.seq
 for i in range(len(dna)-2):
   if dna[i:i+3]=="ATG":
     for j in range(i+3, len(dna)-2, 3):
       codon=dna[j:j+3]
       if codon in ["TAA", "TAG", "TGA"]:
         orf=dna[i:j+3]
         print("ORF found:", orf)
         break