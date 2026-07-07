#K-mer counting
from Bio import SeqIO
for record in SeqIO.parse("HPV16.fasta","fasta"):
    seq=record.seq  
k = 4
kmer_count = {}

for i in range(len(seq)-k+1):
        kmer = seq[i:i+k]

        kmer_count[kmer] = kmer_count.get(kmer, 0) + 1

for kmer, count in sorted(kmer_count.items()):
    print(kmer, count)