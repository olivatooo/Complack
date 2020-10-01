from constants import *
import settings as s
import subroutines as subs
from handleFunctions import *
import sys

if __name__ == "__main__":
    try:
        file = open(sys.argv[1])
        code = file.read()
        code = code.splitlines()
    except:
        print("Usage:")
        print("python", sys.argv[0], "simplackexProgram")
        exit(1)

    s.init()
    # TODO: Move this to settings
    code = subs.cleanCode(code)
    subs.mapCode(code)
    while not s.finished:
        l = code[s.point].strip()
        line = l.split()
        ins = line[0]
        if s.debug == True:
            print("Instruction:", l)
            print("Stack:", s.stack)

        # It's a commentary
        if l[0] == '#':
            s.point += 1
        elif ins == iInput:
            handleInput(line[1])
        elif ins == iOutput:
            handleOutput(line[1], line[2])
        elif ins == iPush:
            handleStackPush(line[1])
        elif ins == iPop:
            handleStackPop(line[1])
        elif ins == iIncrease:
            handleIncrease(line)
        elif ins == iSet:
            handleSet(line)
            
        # Conditional branching
        elif ins == cEqual:
            handleIf(line, cEqual)
        elif ins == cNotEqual:
            handleIf(line, cNotEqual)
        elif ins == cBigger:
            handleIf(line, cBigger)
        elif ins == cSmaller:
            handleIf(line, cSmaller)
        
        elif ins == iGoSub:
            handleSubroutine(line[1])
        elif ins == subEnd:
            handleEndSubroutine()
        elif ins == iGoto:
            s.point = int(line[1])
        elif ins == iExit:
            s.finished = True
        elif ins == subInit:
            s.callstack.append("#")
            s.point += 1
        if l==code[-1] and ins != iGoto:
            s.finished = True

