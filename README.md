# Bioinformatics with Python: A Beginner's Toolkit

This repository documents my journey into computational biology.Rather than using randomly generated DNA sequences, the analysis in this project is performed on a **real FASTA dataset** containing the complete genome sequence of **Human Papillomavirus Type 16 (HPV16)**.Human Papillomavirus Type 16 (HPV16) is one of the high-risk HPV types associated with several cancers, particularly cervical cancer. Using its genome as an example dataset provides an opportunity to practice computational analysis on a biologically important viral genome.

The DNA sequence used in this project was obtained from the ENA(European Nucleotide Archive) database in FASTA format.Working with an authentic biological dataset allowed me to understand how computational tools are applied to real genomic sequences and provided hands-on experience with biological data commonly available in public databases.

Built while learning the fundamentals of Biopython, sequence manipulation, and data visualization each script and notebook exercise is intentionally kept small and easy to understand, making it suitable for beginners in Python and bioinformatics.

---

# Dataset
- Dataset: Human Papillomavirus Type 16 (HPV16) Complete Genome
- Source: European Nucleotide Archive (ENA)
- Accession Number: K02718
- Format: FASTA

---
# Tools Used

- Python 3
- Biopython
- Matplotlib

---

# Repository Structure

```text
Sample Input File

FASTA Files

Notebook

Bioinformatics-Python-Basics
 fasta_reading.py
 nucleotide_count.py
 nucleotide_count_plot.py
 ATGC_content_calc.py
 ATGC_content_pie_chart.py
 DNA_reversal.py
 DNA_conversion.py
 Amino_acid_freq.py
 Homopolymer_strength_calc.py
 ORF_finder.py
 RE_finder.py
 K-mer_counting.py
 Motif_finder.py
 Common_genes.py

Sample Output

Images 

 
```

---

# The Set Of Analysis Made in Python

There is a notebook containing 14 beginner-friendly exercises covering the fundamentals of biological sequence analysis with sample input of Sequence.fasta file which I preferred using in my first analysing.Then I decided to use real Biological Dataset so that I can explore Databases and it will also increase the value of my project.I have included separate python script of 15 tools or analysing set to analyze the basic fundamentals of Human Pappiloma Virus type 16.

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
#  Why Use a Real Dataset?

Using the HPV16 genome instead of an artificial DNA sequence helps demonstrate how introductory bioinformatics methods can be applied to authentic biological data.

Working with real genomic sequences develops skills that are directly applicable to:

- Computational genomics
- Viral genome analysis
- Sequence annotation
- Biological database exploration
- Reproducible bioinformatics workflows


# Learning Outcomes

Through this project, I learned to:

- Parse and manipulate biological sequence data using Biopython.
- Apply core concepts of DNA, RNA and protein sequence analysis through Python programming.
- Perform basic sequence analysis and motif searching.
- Create simple biological data visualizations using Matplotlib.
- Write clean, modular and beginner-friendly Python programs.
- Organize bioinformatics projects using GitHub.

---



