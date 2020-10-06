"""
def retrieveFile():
    try:
        bestStudent = {}
        bestStudentStr = "The best student ranked\n\n"

        f = open("studentgrades.txt")

    except(IOError), e:
        print "File not found", e

    else:
        for line in f:
            name, grade = line.split()
            bestStudent[grade] = name
        f.close()

        for i in sorted(bestStudent.keys(), reverse = True):

            print (bestStudent[i] + ' scored a ' + i)
            bestStudentStr += bestStudent[i] + ' scored a ' + i + '\n'
        print '\n'

        print bestStudentStr

        outToFile = open("studentrank.txt", "w")
        outToFile.write(bestStudentStr)
        outToFile.close()

        print "Finished Output"

    return


def main():
    retrieveFile()


if __name__ == '__main__' : main()
"""

import os

def directoryPlay():
    print os.listdir("/usr")

    print os.path.isdir("/usr/bin/python")
    print os.path.isfile("/usr/bin/python")

    dirList = os.listdir("/usr")

    for file in dirList:
        if os.path.isdir("/usr/" + file):
            print os.listdir("/usr/" + file)
        else:
            continue

    #os.mkdir("") # create a new directory / specify the path between the quotation marks
    #os.rmdir("") # remove a directory

    return


def main():
    directoryPlay()

if __name__ == '__main__' : main()