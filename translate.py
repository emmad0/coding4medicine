f = open("/share/SARS-class/SARS-2020.fasta")

lines = f.readlines()

seq = ""

for i in range(1,len(lines)):
    seq += lines[i].rstrip('\n')

def translation(seq, start):
    seqlen = range(start,len(seq),3)

    aminoacids = {
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

    translation = ""

    for i in seqlen:
        if i > len(seq)-3:
            break
        else:
            translation += aminoacids[seq[i:i+3]]

    return translation


def findproteins(aminos):
    count = 0
    start = False
    proteins = ""
    aminostemp = ""
    aminoacids = ["I", "M", "T", "N", "K", 'S', 'R', 'L', 'P', 'H', 'Q', 'R', 'V', 'A', 'D', 'E', 'G', 'S', 'F', 'L', 'Y', 'C', "W"]

    for i in aminos:
        if i == "M" and start == False:
            aminostemp = "M"
            start = True
            count += 1
        elif i in aminoacids:
            aminostemp += i
            count += 1
        elif i == "*":
            aminostemp += "*"
            if count > 100:
                proteins += aminostemp + "\n"
            aminostemp = ""
            count = 0
            start = False

    return(proteins)

    '''for a in aminos:
            if start == True:
                    aminostr += str(a)
                    count +=1
            if a == "M" and start == False:
                    start = True
                    count += 1
                    aminostr = "M"
            if a == "*" and start == True:
                    start = False
                    if count > 100:
                            proteins += aminostr
                            print(proteins)
                            print()
                            print(count)
                            print()
                    count = 0'''












'''def findproteins(aminos):
	count = 0
	start = False
	proteins = []
	for a in aminos:
		if start == True:
			aminolist.append(a)
			count +=1
		if a == "M" and start == False:
			start = True
			count += 1
			aminolist = ["M"]
		if a == "*" and start == True:
			start = False
			if count > 100:
				proteins.append(aminolist)
				count = 0
	return (proteins)
'''
x = translation(seq, 0)
# print(x)

# print()

y = translation(seq, 1)
# print(y)

# print()

z = translation(seq, 2)
# print(z)

print(findproteins(x))
print()
print(findproteins(y))
print()
print(findproteins(z))
