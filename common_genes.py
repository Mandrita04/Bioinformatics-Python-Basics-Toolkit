#Finding common genes between two experiments

genes_exp1 = input("Enter 1st genomic sequence: ").split()
genes_exp2 = input("Enter 2nd genomic sequence: ").split()

set1 = set(genes_exp1)
set2 = set(genes_exp2)

common_genes = set1.intersection(set2)

print("Common Genes:")
print(common_genes)

print("Number of common genes:", len(common_genes))