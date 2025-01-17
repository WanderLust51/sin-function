from math import sin
import time
import os

def cutString(x,string):
    string

    while len(string) < x:
        string = string*2
    
    return string[0:x]

def raimbowText(num,string):
    return(f'\033[38;2;{160};20;{num*3}m{string}\033[0m')

def rightSide(num, string):
    spaceMax = os.get_terminal_size().columns
    #spaceNum = spaceMax - len(string)
    spaceNum = spaceMax - num
    spaces = cutString(spaceNum, ' ')
    rightString = str(spaces + string)
    return rightString

i = 1
num = 0
terminalWidth = os.get_terminal_size().columns

while True:
    num = int((sin(i/10)+1)*40)

    #print(cutString(num,'pronto todo acabará '))
    #print(raimbowText(num,cutString(num,'#')))
    #print(rightSide(num, raimbowText(num,cutString(num,'#'))))

    

    i = i + 1
    time.sleep(0.05)


    