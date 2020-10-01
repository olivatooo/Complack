import settings as s
from constants import *

def handleInput(typeOfInput):
    # Receives a string
    if typeOfInput == typeAppend:
        inp = input('>>')
        for i in inp:
            try:
                s.stack.append(ord(i))
            except:
                print("Not and ordinal number :", i, "str :",inp)

    # Receives a int
    elif typeOfInput == typeInt:
        inp = input('>>')
        try:
            s.stack.append(int(inp))
        except:
            print("Invalid integer value", inp)
            exit(1)
    s.point += 1


def handleOutput(stackPointer, typeOfOutput):
    item = s.stack[int(stackPointer)]
    if typeOfOutput == typeAppend:
        print(chr(item),end='')
    elif typeOfOutput == typeInt:
        print(item,end='')
    s.point += 1


def handleStackPop(val):
    try:
        s.stack.pop(int(val))
        s.point += 1
    except IndexError:
        print('Pop from empty stack at', val)
        exit(1)


def handleStackPush(val):
    # Maybe enable any type of push?
    s.stack.append(int(val))
    s.point += 1


def handleIncrease(line): 
    add = 0
    try:
        if line[2][0] == sPointer:
            add = s.stack[int(line[2][1:])]
        else:
            add = int(line[2])
        
        s.stack[int(line[1])] = s.stack[int(line[1])] + add
        s.point += 1
    except IndexError:
        print("Invalid INCREASE: ", line)
        exit(0)


def handleSet(line):
    val = 0
    try:
        if line[2][0] == sPointer:
            val = s.stack[int(line[2][1:])]
        else:
            val = int(line[2])
        s.stack[int(line[1])] = val
        s.point += 1
    except IndexError:
        print("Invalid SET:", line)
        exit(0)


def handleIf(line, typeOfCondition):
    try:
        if line[2][0] == sPointer:
            check = s.stack[int(line[2][1:])]
        else:
            check = int(line[2])

        if typeOfCondition == cEqual:
            if s.stack[int(line[1])] == check:
                s.point = int(line[4])
            else:
                s.point += 1

        if typeOfCondition == cNotEqual:
            if s.stack[int(line[1])] != check:
                s.point = int(line[4])
            else:
                s.point += 1

        if typeOfCondition == cBigger:
            if s.stack[int(line[1])] > check:
                s.point = int(line[4])
            else:
                s.point += 1

        if typeOfCondition == cSmaller:
            if s.stack[int(line[1])] < check:
                s.point = int(line[4])
            else:
                s.point += 1
    except IndexError:
        print("Invalid if/nif/bif/sif:", line, typeOfCondition)


def handleSubroutine(subname):
    s.callstack.append(s.point)
    try:
        s.point = s.sub[subname]
    except KeyError:
        print("Subroutine name does not exist")
        exit(1)


def handleEndSubroutine():
    try:
        sp = s.callstack.pop()
        if sp != '#':
            s.point = sp
        else:
            s.point += 1
    except:
        print("Calling 'end' without a subroutine")
        exit(1)

