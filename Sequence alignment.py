# Import libraries
from Bio import AlignIO

# Parsing Sequence Alignment
alignment = AlignIO.parse(open("PF18225_seed.txt"), "stockholm")

# Show alignment generator
print(alignment)

# Printing alignment
for alignment in alignments:
	print(alignment)
