from constants import subInit, label, iSwitchStack

# This is called only once in main
def init():
    global stack
    global debug
    global point
    global sub
    global callstack
    global substack
    global gotoMap
    global dictOfStacks
    stack = []
    dictOfStacks = {}
    substack = []
    sub = {}
    gotoMap = {}
    callstack = []
    debug = False
    point = 0


def cleanCode(code):
    cleanedCode = []
    for line in code:
        if line.split() != []:
            cleanedCode.append(line)
    return cleanedCode


def mapCode(code):
    i = 0
    for line in code:
        l = line.split()
        if l[0] == subInit:
            sub[l[1]] = i+1
        if l[0] == label:
            gotoMap[l[1]] = i+1
        if l[0] == iSwitchStack:
            dictOfStacks[l[1]] = []
        i += 1
        

