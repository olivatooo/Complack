import settings as s
from constants import *

def cleanCode(code):
    cleanedCode = []
    for line in code:
        if line.split() != []:
            print(line)
            if line[0] != "#":
                cleanedCode.append(line)
    return cleanedCode


def mapCode(code):
    i = 0
    for line in code:
        l = line.split()
        print(l)
        if l[0] == subInit:
            s.sub[l[1]] = i+1
        i += 1
        

