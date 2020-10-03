import settings as s
from constants import *


def handleSubroutine(subname):
    s.callstack.append(s.point)
    try:
        s.point = s.sub[subname]
    except KeyError:
        print("Subroutine name does not exist", subname)
        exit(1)


def handleInitSubroutine(code):
    s.point += 1
    # Just a marker 
    subDefinitionStack = ["s"]
    while subDefinitionStack != []:
        try:
            l = code[s.point].strip()
        except:
            print("Unclosed subroutine!")
            exit(1)
        line = l.split()
        ins = line[0]
        if ins == subEnd:
            subDefinitionStack.pop()
        if ins == subInit:
            subDefinitionStack.append("s")
        s.point += 1
    

def handleEndSubroutine():
    try:
        sp = s.callstack.pop()
        s.point = sp + 1
    except:
        print("Calling 'end' without a subroutine")
        exit(1)

