#A pie chart showing comparison between GC content and AT content in a DNA sequence
import matplotlib.pyplot as plt
from Bio import SeqIO

for record in SeqIO.parse("HPV16.fasta", "fasta"):
    sequence = record.seq
A = sequence.count("A")
T = sequence.count("T")
G = sequence.count("G")
C = sequence.count("C")

gc = ((G + C) / len(sequence)) * 100
at = ((A + T) / len(sequence)) * 100
print("Length:", len(sequence))
print("GC Content:", gc)

# Pie chart
labels = ['GC Content', 'AT Content']
sizes = [gc, at]

plt.figure(figsize=(6,6))
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("GC vs AT Composition")

plt.show()