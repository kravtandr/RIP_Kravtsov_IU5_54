from math import sqrt
import re

def main():
    solveBiquard(getExpressionVar())


def getExpressionVar():
    var = []
    for i in range(3):
        unCorrectVar = True
        while unCorrectVar:
            var.append(input())
            if re.match(r'\-*\d+', var[i]):
                unCorrectVar = False
            else:
                var.pop()
    return list(map(float, var))


def solveBiquard(var):

    Flag = 5
    x1,x2,x3,x4 = None,None,None,None
    diskr = var[1]**2 - 4 * var[0] * var[2]
    if diskr < 0:
        print("Нет действительных корней")
    if diskr == 0:
        Flag = 5
        if 2 * var[0] != 0 and (-1 * var[1]) / (2 * var[0]) >= 0:
            Flag = 1
            x1 = sqrt((-var[1]) / (2 * var[0]))
            x2 = x1 * -1
    if diskr > 0:
        x1 = (-var[1] + sqrt(diskr)) / (2 * var[0])
        x3 = (-var[1] - sqrt(diskr)) / (2 * var[0])
        if x1 >= 0:
            Flag = 1
            x1 = sqrt(x1)
            x2 = x1 * -1
        if x3 >= 0:
            if Flag == 1:
                Flag = 3
            else:
                Flag = 2
                x3 = sqrt(x3)
                x4 = x3 * (-1)

    printSolution(Flag, x1, x2, x3, x4)


def printSolution(Flag, *args):
    if Flag == 0:
        print("Нет действительных корней")
    elif Flag == 1:
        if args[0] != args[1] and args[0] != None and args[1] != None:
            print("Уравнение имеет два корня:") 
            print(args[0], args[1])
        else:
            print("Уравнение имеет один корень:")
            print(args[0])

    elif Flag == 2:
        if args[2] != args[3] and args[2] != None and args[3] != None:
            print("Уравнение имеет два корня:")
            print(args[2], args[3])
        else:
            print("Уравнение имеет один корень:")
            print(args[2])
    elif Flag == 3:
        if args[0] != args[1] and args[2] != args[3] and args[0] != None and args[1] != None and args[2] != None and args[3] != None:
            print("Уравнение имеет четыре корня:")
            print(args[0], args[1],  args[2], args[3])
        
        else:
            if args[0] != args[1] and args[0] != None and args[1] != None:
                print("Уравнение имеет три корня:")
                print(args[0], args[1], args[2])
            else:
                print("Уравнение имеет три корня:")
                print(args[1],  args[2], args[3])
    elif Flag == 4:
        if args[0] != args[1] and args[0] != None and args[1] != None:
            print("Уравнение имеет два корня:")
            print(args[0], args[1])
        else:
            print("Уравнение имеет один корень:")
            print(args[0])
    elif Flag == 5:
        print("Нет действительных корней")


main()