f = open("/share/SARS-class/SARS-2020.fasta")
line = f.readline()
lines = f.readlines()
dna = ""
for a in lines:
	dna+=a.rstrip("\n")
protein1 = []
aminos = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'}


start = False
for i in range(0, len(dna)-2, 3):
    codon = dna[i:i+3]
    protein1.append(aminos[codon])
print (protein1)
print ("\n")
protein2 = []
for i in range(1, len(dna)-2, 3):
    codon = dna[i:i+3]
    protein2.append(aminos[codon])
print (protein2)
print ("\n")
protein3 = []
for i in range(2, len(dna)-2, 3):
    codon = dna[i:i+3]
    protein3.append(aminos[codon])
print (protein3)

for i in protein1:

