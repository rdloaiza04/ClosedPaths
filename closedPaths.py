import time
import os
"""
Function where the number is received via parameters or defined by an input.
I: num(Integer) can be None
O: result(Integer)
"""
def closedPaths(num = None):
    if num == None:
        invalidInput = True
        while(invalidInput):
            try:
                num = int(input("\nEnter a number: "))
                invalidInput = False
            except:
                print("Please enter a valid number")
                time.sleep(2)
    return pathCalculator(num)

"""
This function calculates the total number of paths in a number
I: value(Integer)
O: result(Integer)
"""
def pathCalculator(value):
    zeroNum = [1, 2, 3, 5, 7]
    result = 0
    defValue = value
    while(defValue != 0):
        evalNum = defValue%10
        if evalNum == 8:
            result += 2
        elif not evalNum in zeroNum:
            result += 1
        defValue//=10
    printOutput(str(value), str(result))
    return result   

"""
Funtion that print the result
I: value(Integer), result(Integer)
O: None
"""
def printOutput(value, result):
    numSize = len(value)
    if numSize > 14:
        divLines = "-" * numSize
        whiteSpaces = " "*(numSize - 2)
        numWhite = " "*4
    else:
        whiteSpaces = " "*12
        divLines = "-"*14
        numWhite = " "*(18 - numSize)
    print("\n    -------- Closed Paths ----------\n\n  STDIN" + 
          whiteSpaces+ "Function" + whiteSpaces + "Result\n" + 
          (divLines + " -> ")*2 + "-"*10+ "-\n"+
          (value + numWhite)*2+result)
    

#closedPaths()
closedPaths(630) #result = 2
closedPaths(1288) #result = 4
closedPaths(98883) #result = 7