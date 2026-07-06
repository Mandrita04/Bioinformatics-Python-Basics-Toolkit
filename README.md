# Bioinformatics with Python: A Beginner's Toolkit

This repository documents my journey into computational biology, starting from the basics reading FASTA files, counting nucleotides, translating sequences, and visualizing sequence composition all the way to simple motif search and gene set comparison.

Built while learning the fundamentals of Biopython, sequence manipulation, and data visualization each script and notebook exercise is intentionally kept small and easy to understand, making it suitable for beginners in Python and bioinformatics.

---

# Tools Used

- Python 3
- Biopython
- Matplotlib

---

# Repository Structure

```text
Bioinformatics-Python-Basics

 Bioinformatics tool.ipynb
 ATGC_count.py
 ATGC_content_pie_chart.py
 Amino_acid_freq.py

 
```

---

# Jupyter Notebook Exercises

The notebook contains 14 beginner-friendly exercises covering the fundamentals of biological sequence analysis.

| No. | Exercise | Description |
|:---:|----------|-------------|
| 1 | Reading a FASTA File | Parses a FASTA file and prints the sequence ID and sequence |
| 2 | DNA Nucleotide Count | Counts the number of A, T, G and C nucleotides |
| 3 | ATGC Content Calculator | Calculates the GC percentage of a DNA sequence |
| 4 | Reverse Complement | Generates the reverse complement of a DNA sequence |
| 5 | DNA → RNA Conversion | Transcribes DNA into RNA |
| 6 | DNA → Protein Conversion | Translates DNA into a protein sequence |
| 7 | ORF Finder | Detects Open Reading Frames between start and stop codons |
| 8 | Restriction Enzyme Site Finder | Locates EcoRI, BamHI and HindIII restriction sites |
| 9 | K-mer Counting | Counts all k-mers in a DNA sequence (default: k = 4) |
| 10 | Extract Specific Sequence | Searches for a user-defined motif within a FASTA sequence |
| 11 | Multiline → Single-line FASTA | Converts multiline FASTA into single-line FASTA format |
| 12 | Motif Finding | Finds every occurrence of a specified motif |
| 13 | Homopolymer Strength | Identifies the longest consecutive run of the same nucleotide |
| 14 | Common Genes Between Experiments | Finds overlapping genes using Python set operations |

---

#  Python Scripts

## 1. ATGC_count.py

Reads a FASTA file and generates a bar chart showing the frequency of each nucleotide (A, T, G and C).

---

## 2. ATGC_content_pie_chart.py

Calculates the GC content and AT content of a DNA sequence and displays the results using a pie chart.

---

## 3. Amino_acid_freq.py

Translates a DNA sequence into a protein sequence and visualizes the frequency of each amino acid using a bar chart.

---

# Learning Outcomes

Through this project, I learned to:

- Parse and manipulate biological sequence data using Biopython.
- Apply core concepts of DNA, RNA and protein sequence analysis through Python programming.
- Perform basic sequence analysis and motif searching.
- Create simple biological data visualizations using Matplotlib.
- Write clean, modular and beginner-friendly Python programs.
- Organize bioinformatics projects using GitHub.

---

#  Future Improvements

- Add error handling for missing or invalid FASTA files.
- Convert repeated FASTA parsing code into reusable functions/modules.
- Add unit tests for each program.
- Extend the ORF finder to detect all six reading frames.
- Support multiple FASTA sequences in all analysis scripts.
- Add command-line arguments for improved usability.

---

