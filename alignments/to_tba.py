import sys,re

files = """
arboricola/GCA_000292725.1_SacArb1.0_genomic.fna
cerevisae/GCF_000146045.2_R64_genomic.fna
eubayanus/GCA_001298625.1_SEUB3.0_genomic.fna
kudriavzevii/GCA_000256765.1_Saccharomyces_kudriavzevii_strain_FM1066_v1.0_genomic.fna
mikatae/GCA_000167055.1_ASM16705v1_genomic.fna
paradoxus/GCA_000166955.1_ASM16695v1_genomic.fna
uvarum/GCA_000166995.1_ASM16699v1_genomic.fna
"""
files = files.strip().split('\n')

for f in files:
    print(f)
    name = "sac"+f[:3].capitalize()
    proc = open(name+".fa", "w")
    out = []
    chr_counter = 1
    for l in open(f):
        if ">" in l:
            out.append([">%s:%s:1:+:"%(name, str(chr_counter)),""])
            chr_counter += 1
        
    	else:
            res = re.sub("\ +.+","",l)
            res = re.sub("\.","_",res)
            out[-1][1]+=res
    for org in out:
        proc.write(org[0]+str(len(org[1]))+'\n' + org[1])
    proc.close()
