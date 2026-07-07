#DNA to protein conversion
from Bio import SeqIO
for record in SeqIO.parse("HPV16.fasta","fasta"):
    dna=record.seq
    rna=dna.transcribe()
    pr1=dna.translate()
print("RNA sequence from DNA:", rna)
print("Protein sequence from DNA:", pr1)