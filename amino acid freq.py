#Finding out the frequency of amino acid in a protein sequence 
#Plottting the frequency of amino acid in protein sequenceusing bar chart
from Bio import SeqIO
import matplotlib.pyplot as plt
for record in SeqIO.parse("HPV16.fasta","fasta"):
    dna=record.seq
    
    pr1=dna.translate()    
print("Protein sequence from DNA:", pr1)
amino_acids = []
frequency = []

for aa in sorted(set(pr1)):
    if aa != "*":
        amino_acids.append(aa)
        frequency.append(pr1.count(aa))

plt.bar(amino_acids, frequency)

plt.title("Amino Acid Frequency")
plt.xlabel("Amino Acids")
plt.ylabel("Frequency")

plt.show()