import display
import structures
from Queue import *
from copy import deepcopy

def isLegalMove(tempx, tempy):
    if tempx < 0 or tempx > 2:
        return False

    if tempy < 0 or tempy > 2:
        return False

    return True

def switchMove(index):
    switcher = {
        0: "N",
        1: "E",
        2: "S",
        3: "W"
    }

    return switcher.get(index)

class PuzzleModel:

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.startState = structures.Node(puzzle) #puzzle = array de int uri

    def solveFunction(self):
        print("solving shit")

        #print("Considering BFS: ", self.BFS())
        print("Considering DFS: ", self.IDDFS())
        #print("Considering Greedy with Manhattan Distance Heuristic", self.greedySearch(0))
        #print("Considering Greedy with Euclidian Distance Heuristic", self.greedySearch(1))
        #print("Considering A* with Manhattan Distance Heuristic", self.aStarSearch(0))
        #print("Considering A* with Euclidian Distance Heuristic", self.aStarSearch(1))

    def isGoalState(self, currentState):
        goalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        #print(currentState.puzzle)
        #print(goalState)

        for i in range(0, 9):
           if (currentState.puzzle[i] != goalState[i]):
                #print("The current state is not the goal state.")
                return False

        #print("The current state is the goal state.")
        return True

    def getSuccessors(self, currentState):
        x = y = tile = 0

        for i in range(0, 9):
            if currentState.puzzle[i] == 0:
                x = i / 3
                y = i % 3
                tile = i
                break

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        successors = Queue()
        for i in range(0, 4):
            tempx = x + dx[i]
            tempy = y + dy[i]

            if isLegalMove(tempx, tempy) == True:
                newPuzzle = deepcopy(currentState.puzzle)
                newTile = tempx * 3 + tempy % 3

                newPuzzle[tile] = newPuzzle[newTile]
                newPuzzle[newTile] = 0

                action = switchMove(i)
                #print(action)

                newState = structures.Node(newPuzzle, currentState, action)
                successors.put(newState)

        return successors

    def BFS(self):

        frontier = Queue()
        steps = list()

        frontier.put(self.startState)
        while True:
            if frontier.empty():
                return None # nu gaseste solutie daca vreodata frontiera ajunge goala

            currentState = frontier.get()
            if self.isGoalState(currentState):
                return currentState.actions

            elif currentState not in steps:
                steps.append(currentState)
                successors = self.getSuccessors(currentState)
                while not successors.empty():
                    frontier.put(successors.get())

    # Iterative Deepening Depth-First Search Algorithm
    def IDDFS(self):
        depth = 0
        currentState = None
        while currentState == None:
            currentState = self.DLS(depth)
            depth = depth + 1

        return currentState.actions

    # Depth Limited Search ALgorithm
    def DLS(self, depth):
        frontier = LifoQueue()
        frontier.put(self.startState)

        while True:
            if frontier.empty():
                return None

            currentState = frontier.get()
            if self.isGoalState(currentState):
                return currentState

            elif currentState.depth != depth:
                successors = self.getSuccessors(currentState)
                while not successors.empty():
                    frontier.put(successors.get())

    # nu merge
    def greedySearch(self, type):
        currentState = self.startState

        frontier = PriorityQueue()
        steps = list()

        frontier.put((currentState.heuristic(type), currentState))

        while True:
            if frontier.empty():
                return None

            currentState = frontier.get()[1]

            print(currentState.puzzle)

            if self.isGoalState(currentState):
                print(currentState.actions)
                return currentState

            elif currentState not in steps:
                steps.append(currentState)
                successors = self.getSuccessors(currentState)

                while not successors.empty():
                    successor = successors.get()
                    frontier.put((successor.heuristic(type), successor))

    def aStarSearch(self, type):
        currentState = self.startState
        frontier = PriorityQueue()
        frontier.put((currentState.heuristic(type), currentState))
        steps = list()

        while True:
            if frontier.empty():
                return None

            currentState = frontier.get()[1]
            if self.isGoalState(currentState):
                print(currentState.actions)
                return currentState

            elif currentState not in steps:
                steps.append(currentState)
                successors = self.getSuccessors(currentState)

                while not successors.empty():
                    successor = successors.get()
                    frontier.put((successor.heuristic(type) + successor.depth, successor))