import argparse
import re

parser = argparse.ArgumentParser(description='a code to explore motif explore motif diversity')
parser.add_argument("-i", '--input', help="input a fasta file")
parser.add_argument("-m", '--motif', help="input a motif in regular expression")
parser.add_argument("-o", '--output', help="the out put file name")

args = parser.parse_args()

inf = open(args.input)
ouf = args.output
motif = args.motif
regex = re.compile(motif)

def readseq(fasta):# return a dict in which headers are keys and sequences are value
    seq = {}
    for line in fasta:
        if line.startswith(">"):
            name = line.replace('>','').split()[0]
            seq[name] = ''
        else:
            seq[name]+=line.replace('\n','').strip()
    return seq
seq = readseq(inf)
ofile = open(ouf,'w')
print('header'+'    '+'tax',file=ofile)

for key in seq:
    sequence = str(seq[key])
    if re.search(regex,str(seq[key])) != None:
        fragment = re.findall(regex,str(seq[key]))[0]
        header = key.split('|')[1] #This line is to deal with raw uniprot ID :>tr|ID|annotations
        print(header+'    '+fragment[-3:],file=ofile)
ofile.close()
