"""
def addNumbers(num1 = 1, num2 = 1):
    return num1 + num2

def main ():
    #pass
    #print addNumbers()
    print addNumbers(50, 60)

if __name__ == '__main__' : main() # what function to call when the program starts
"""

"""
globalTen = 10

def addNumbers(*args):
    print globalTen
    
    globalTen = 15
    
    result = 0

    if args:
        for i in args:
            result += i
        return result # local variabile only visible in the addNumbers namespace
    else:
        return "Please provide numbers"

def main ():
    print globalTen
    
    print addNumbers(50, 60, 60, 50)

if __name__ == '__main__' : main() # what function to call when the program starts
"""

"""
# how to change the value of a global variable from inside of a function - modality 1

globalTen = 10

def changeGlobal():
    global globalTen
    globalTen = 15

def main():
    print globalTen
    changeGlobal()
    print globalTen

if __name__ == '__main__': main()
"""

"""
# how to change the value of a global variable from inside of a function - modality 2

globalTen = 10

def changeGlobal():
    globals()['globalTen'] = 20

def main():
    print globalTen
    changeGlobal()
    print globalTen

if __name__ == '__main__': main()
"""

"""
# how to pass an unlimited number of key-value pairs for processing inside of a function

def createDict(**kvargs):
    for i in kvargs:
        print i, kvargs[i]
    print type(kvargs)
    return


def main():
    # createDict(Name = 'iolia', Age = 21, YearBorn = 1999)
    createDict(Cust1=('iolia', 21, 1999), Cust2=('spongebob', 34, 1986))


if __name__ == '__main__': main()
"""

# recursion

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def main():
    print factorial(4)

if __name__ == '__main__': main()