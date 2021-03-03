from Queue import Queue

class Node:
    def __init__(self, puzzle, parent=None, action=""):
        self.puzzle = puzzle
        self.parent = parent


        if parent is None:
            self.depth = 0
            self.actions = ""
        else:
            self.depth = self.parent.depth + 1
            self.actions = self.parent.actions + action

    def heuristic(self, type):
        if type == 0:
            return self.manhattanDistance()
        else: # type == 1
            return self.numberOfWrongTiles()

    def manhattanDistance(self):
        finaldistance = 0

        for i in range(0, 3):
            for j in range(0, 3):
                tile = i * 3 + j % 3
                index = self.puzzle[tile] - 1

                if index == -1:
                    distance = (2 - i) + (2 - j)
                else:
                    distance = abs(i - (index / 3)) + abs (j - (index % 3))

                finaldistance = finaldistance + distance

        return finaldistance

    def numberOfWrongTiles(self):
        total = 0
        count = 1

        for i in range(0, 3):
            for j in range(0, 3):
                tile = i * 3 + j % 3
                if self.puzzle[tile] != (count % 9):
                    total = total + 1
                count = count + 1

        return total