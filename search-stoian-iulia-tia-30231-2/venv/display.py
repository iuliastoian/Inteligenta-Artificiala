from Tkinter import *
import tkFont
import os
import sys
from model import *


from random import randint

def main():
    root = Tk()
    app = PuzzleWindow(root)


class PuzzleWindow:

    def __init__(self,master):
        self.master = master
        self.master.title("8 PUZZLE")
        self.master.geometry("220x400+900+200")
        self.master.resizable(0, 0)
        self.master.config(bg="#5DADE2")
        self.frame = Frame(self.master, background="#D6EAF8")
        self.frame.pack()

        self.goalWindow = Toplevel()
        self.goalWindow.geometry("250x300+1123+200")
        rootPath = os.path.dirname(os.path.abspath("goalState.gif"))
        rootPath = rootPath[:-4]
        rootPath = rootPath + "goalState.gif"
        goalImage = PhotoImage(file=rootPath)
        goalLabel = Label(self.goalWindow, image=goalImage)
        goalLabel.image = goalImage
        goalLabel.pack()
        self.goalWindow.overrideredirect(1)
        #.deiconify()




        shuffleFrame = LabelFrame(self.frame, width=300, height=50, background="#5DADE2")
        puzzleFrame = LabelFrame(self.frame, width=300, height=300, background="#2874A6")
        solutionFrame = LabelFrame(self.frame, width=300, height=120, background="#AED6F1")
        shuffleFrame.pack()
        puzzleFrame.pack()
        solutionFrame.pack()

        # SHUFFLE FRAME
        shuffleButton = Button(shuffleFrame,  text="SHUFFLE", command = self.shuffleFunction, bd=4, bg="#7FB3D5",width=10, height=1, font=tkFont.BOLD ).pack(side=LEFT)

        self.showGoal = IntVar(value=1)
        showGoalButton = Checkbutton(shuffleFrame, text="show GOAL", variable=self.showGoal, command = self.showGoalFunction, bd = 1, bg="#7FB3D5", width=10, height=1).pack(side=RIGHT)


        # PUZZLE FRAME
        self.puzzleCells = []
        #self.emptyCell = self.puzzleCells[0]
        noOfCells = 0

        # initialize puzzle
        for i in range (3):
            for j in range (3):
                cell = Label(puzzleFrame, text = str(noOfCells),borderwidth=2,relief="groove",  width=5, height=3, font=tkFont.BOLD, bg="#AED6F1")
                cell.grid(row = i, column = j)
                self.puzzleCells.append(cell)
                noOfCells = noOfCells + 1
        self.puzzleCells[0].config(text = "")
        self.emptyCellIndexGlobal = 0
        self.inputPuzzle = []

        # SOLUTION FRAME
        solutionLabel = Label(solutionFrame, text = "SOLUTION:", font = tkFont.NORMAL, bg="#D4E6F1").pack(side=LEFT)
        solveButton = Button(solutionFrame,  text="SOLVE", command = self.solveFunction, bd=4, bg="#7FB3D5",width=10, height=1, font=tkFont.BOLD ).pack(side=RIGHT)




        self.master.mainloop()

    # SHUFFLE FRAME
    def showGoalFunction (self):
        choose = self.showGoal.get()

        if choose:
            # publici fereastra
            self.goalWindow.deiconify()

        else:
            # ascunzi fereastra
            self.goalWindow.withdraw()

    def shuffleFunction(self):
        #reset the inputPuzzle
        self.inputPuzzle = []

        emptyCellIndex = self.emptyCellIndexGlobal
        permutations = randint(10,30)
        for i in range (0, permutations):
            successors = self.getSuccessors(emptyCellIndex) # get successors
            randomSuccessorIndex = successors[randint(0, len(successors)) - 1] # pick a random successor


            currentLabel = self.puzzleCells[emptyCellIndex]
            successorLabel = self.puzzleCells[randomSuccessorIndex]
            successorValue = successorLabel['text']

            currentLabel.configure(text=successorValue)
            successorLabel.configure(text='')

            emptyCellIndex = randomSuccessorIndex
            self.emptyCellIndexGlobal = emptyCellIndex


    # PUZZLE FRAME

    def getSuccessors(self, cellIndex):
        #cellIndex = self.puzzleCells.index(cell) # position of cell in puzzleCells list
        row = cellIndex / 3 # position of cell in context
        col = cellIndex % 3 # of matrix

        successors = []

        if (row > 0): # not on the first row
            successors.append(cellIndex - 3) # add the NORTH succesor
        if (col < 2): # not on the right col
            successors.append(cellIndex + 1) # add the EAST succesor
        if (row < 2): # not on the last row
            successors.append(cellIndex + 3) # add the SOUTH succesor
        if (col > 0): # not on the left col
            successors.append(cellIndex - 1) # add the WEST succesor

        return successors



    def solveFunction(self):
        self.transferPuzzle()
        #print ("before")
        #print self.inputPuzzle
        self.model = PuzzleModel(self.inputPuzzle)
        #print ("after")
        #print self.inputPuzzle

        self.model.solveFunction()


    def transferPuzzle (self):
        count = 0
        for i in range(0,3):
            for j in range(0,3):
                labelText = self.puzzleCells[count].cget("text")
                if (labelText  == ''):
                    self.inputPuzzle.append(0)
                else:
                    self.inputPuzzle.append(int(labelText))
                count = count + 1




if __name__ == '__main__':
    main()


