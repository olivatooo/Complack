
# This is called only once in main
def init():
    global stack
    global finished
    global debug
    global point
    global sub
    global callstack
    stack = []
    sub = {}
    callstack = []
    finished = False
    debug = True 
    point = 0

