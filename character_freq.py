hello = """TCATCCGACGCCGAGGCTAATAGCAATTGACGTGGGTAGTACCTAGGGTAACATTACATG
GACCTCCTGTCGCACCTTTACTTCGCAGGGAGCTGCTTCGTACACGCGCTGTTCAGCCTA
AGTTTTCTGGCGCAGACTTACTCGGTTCGTCAGACCACCGTTATCGTGTTTATTAGTTTG
AGGAAATAGCTCCCTCGAAGTAGTGCAGTGCGGGGGCGAGCCAAACAAGGGGGCTCCGCG
CTACCTATTGTTCATTTCGGTGAGACAGTAACTAGTCGTTCGATAGCCGGCAAGCCTAAA
GCCTATTCGCAGTCCCATCAATAGGGGCATATGAATAGTTCCTGGGTTCCGTAAGTCCAG
ATTGCCCACAGGTACACTATTTAGTGCTGGGTGTGGTTGGTGCTCACTGCTTCTTGGGGC
ATGAAAGCGTATCCTTTTAACACTGTACGTGGAAGACTTTGAAACGGCCCTGCAGGCACT
ACTCGCGGTTGATAAAAGGCCGCGACGTAAAAAAACCATGTCAATTCGAACGAGGCACGA
TCACACCAATCATCTACTACGCCTGTATTAAACGGGAAAGGCACGGCCGAGGTAGAGTAC
TAGCTCCCAGTGGATACCGTTGAAGAGCGATTTAGTTACAAGATATTAACATTTGGGTAG
GTGGAGTCGTGTCAGTCTAACCCGCTGTCACGGTAGAAGTTGGATCGTAAAGTGAATGGA
ACACTCCCAGCCTTGCCTCAACCCGCATGATAGAAAAGATATCGAAGGGATAAAGCAGCT
AGGGGAGGATCAAGACTTTCTTGTGTCAAAACTCTTATCTTTGACCGCGATACTTCTGGA
TCGAGGATAGCTACTGGAGATATGTTACGGAGATTAGACGCCCGAAGATTTTTACAGTTT
CACTTTCCTTGTAGATTG"""
tally_c = 0
tally_g = 0
tally_a = 0
tally_t = 0
count = 0
for letter in hello:
    if letter == 'C':
        tally_c +=1
    if letter == 'G':
        tally_g +=1
    if letter == 'A':
        tally_a +=1
    if letter == 'T':
        tally_t +=1
    count +=1
print("total: " + str(count)) 
print("C: " + str(tally_c) + " G: " + str(tally_g) + " A: " + str(tally_a) + " T: " + str(tally_t))

per_C = tally_c / count * 100
print(per_C)
per_G = tally_g / count * 100
print(per_G)
per_A = tally_a / count * 100
print(per_A)
per_T = tally_t / count * 100
print(per_T)
print("C%: " + str(per_C) + " G%: " + str(per_G))
