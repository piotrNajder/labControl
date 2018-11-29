import random

IN = 1
OUT = 2

LOW = 3
HIGH = 4

inputsList = list()

def setup(ioName, dir):
    pass

def output(ioName, state):
    pass

def input(ioName):    
    io = next((x for x in inputsList if x["inNum"] == ioName), None)
    if io == None:
        inputsList.append({"inNum": ioName, "state": 1})
    if io["state"] == 1:
        if(random.randint(0, 5001) < 2):
            io["state"] = 0
            return False
        else:
            return True
    else:
        return False

def cleanup():
    pass