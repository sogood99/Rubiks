from enum import Enum
import numpy as np
from copy import deepcopy
from typing import List

# USES IF STATEMENTS FOR BETTER COMPUTE TIMES

class color(Enum):
    noColor = 0
    red = 1
    yellow = 2
    green = 3
    white = 4
    blue = 5
    orange = 6

class direction(Enum):
    horz = 0
    vert = 1
    sides = 2

class Rubiks:
    def __init__(self, n:int):
        self.size = n
        self.config = np.array([[[color.noColor for j in range(n)] for i in range(n)] for _ in range(6)])
    def action(self, dir:direction, isRev:bool, num:int)->"Rubiks":
        """
        action on new config
        dir gives direction of twist
        isRev to set if twist in reverse
        num is row/col num, from 0 -> self.size-1
        returns new rubiks
        """
        newRubiks = deepcopy(self)
        newRubiks.actionSelf(dir, isRev, num)
        return newRubiks


    def actionSelf(self, dir:direction, isRev:bool, num:int)->None:
        """
        action on self
        dir gives direction of twist
        isRev to set if twist in reverse
        num is row/col num, from 0 -> self.size-1
        returns none
        """
        reflectedNum = self.size - 1 - num
        if (dir == direction.horz):
            """horz"""
            if (not isRev):
                # faces = [0,5,2,4]

                last = self.config[0][num][self.size-1]
                for i in range(self.size-1, 0, -1):# doesn't include first element
                    self.config[0][num][i] = self.config[0][num][i-1]

                temp = self.config[5][num][self.size-1]
                for i in range(self.size-1, 0, -1):# doesn't include first element
                    self.config[5][num][i] = self.config[5][num][i-1]
                self.config[5][num][0] = last
                last = temp

                temp = self.config[2][reflectedNum][0]
                for i in range(self.size-1):# doesn't include first element
                    self.config[2][reflectedNum][i] = self.config[2][reflectedNum][i+1]
                self.config[2][reflectedNum][self.size-1] = last
                last = temp

                temp = self.config[5][num][self.size-1]
                for i in range(self.size-1, 0, -1):# doesn't include first element
                    self.config[4][num][i] = self.config[4][num][i-1]
                self.config[4][num][0] = last
                last = temp

                self.config[0][num][0] = last

                if (num == 0):
                    self.config[3] = np.rot90(self.config[3])
                elif (num == self.size-1):
                    self.config[1] = np.rot90(self.config[1], -1)

            else:
                # faces = [0,4,2,5]
                last = self.config[0][num][0]
                for i in range(self.size-1):# doesn't include first element
                    self.config[0][num][i] = self.config[0][num][i+1]

                temp = self.config[4][num][0]
                for i in range(self.size-1):# doesn't include first element
                    self.config[4][num][i] = self.config[4][num][i+1]
                self.config[4][num][self.size-1] = last
                last = temp

                temp = self.config[2][reflectedNum][self.size-1]
                for i in range(self.size-1, 0, -1):# doesn't include first element
                    self.config[2][reflectedNum][i] = self.config[2][reflectedNum][i-1]
                self.config[2][reflectedNum][0] = last
                last = temp

                temp = self.config[5][num][0]
                for i in range(self.size-1):# doesn't include first element
                    self.config[5][num][i] = self.config[5][num][i+1]
                self.config[5][num][self.size-1] = last
                last = temp

                self.config[0][num][self.size-1] = last
                if (num == 0):
                    self.config[3] = np.rot90(self.config[3], -1)
                elif (num == self.size-1):
                    self.config[1] = np.rot90(self.config[1])
            last = None

        elif(dir == direction.vert):
            """vert"""
            if (not isRev):
                # uses [0,3,2,1]
                last = self.config[0][0][num]
                for i in range(self.size-1):# doesn't include first element
                    self.config[0][i][num] = self.config[0][i+1][num]

                temp = self.config[3][0][num]
                for i in range(self.size-1):# doesn't include first element
                    self.config[3][i][num] = self.config[3][i+1][num]
                self.config[3][self.size-1][num] = last
                last = temp

                temp = self.config[2][0][num]
                for i in range(self.size-1):# doesn't include first element
                    self.config[2][i][num] = self.config[2][i+1][num]
                self.config[2][self.size-1][num] = last
                last = temp

                temp = self.config[1][0][num]
                for i in range(self.size-1):# doesn't include first element
                    self.config[1][i][num] = self.config[1][i + 1][num]
                self.config[1][self.size - 1][num] = last
                last = temp

                self.config[0][self.size-1][num] = last

                if (num == 0):
                    self.config[4] = np.rot90(self.config[4])
                elif (num == self.size-1):
                    self.config[5] = np.rot90(self.config[5], -1)

            else:
                # uses [0,1,2,3]
                last = self.config[0][self.size-1][num]
                for i in range(self.size-1, 0, -1):# doesn't include first element
                    self.config[0][i][num] = self.config[0][i-1][num]

                temp = self.config[1][self.size-1][num]
                for i in range(self.size-1, 0, -1):# doesn't include first element
                    self.config[1][i][num] = self.config[1][i - 1][num]
                self.config[1][0][num] = last
                last = temp

                temp = self.config[2][self.size-1][num]
                for i in range(self.size-1, 0, -1):# doesn't include first element
                    self.config[2][i][num] = self.config[2][i-1][num]
                self.config[2][0][num] = last
                last = temp

                temp = self.config[3][self.size-1][num]
                for i in range(self.size-1, 0, -1):  # doesn't include first element
                    self.config[3][i][num] = self.config[3][i - 1][num]
                self.config[3][self.size-1][num] = last
                last = temp

                self.config[0][0][num] = last

                if (num == 0):
                    self.config[4] = np.rot90(self.config[4], -1)
                elif (num == self.size-1):
                    self.config[5] = np.rot90(self.config[5])

        elif (dir == direction.sides):
            """sides"""
            if (not isRev):
                # goes through [5,1,4,3]
                last = self.config[5][self.size-1][num]
                for i in range(self.size-1, 0, -1):# doesn't include first element
                    self.config[5][i][num] = self.config[5][i-1][num]

                temp = self.config[1][reflectedNum][0]
                for i in range(self.size-1):# doesn't include first element
                    self.config[1][reflectedNum][i] = self.config[1][reflectedNum][i+1]
                self.config[1][reflectedNum][self.size-1] = last
                last = temp

                temp = self.config[4][0][num]
                for i in range(self.size-1):# doesn't include first element
                    self.config[4][i][num] = self.config[4][i+1][num]
                self.config[4][self.size-1][num] = last
                last = temp

                temp = self.config[3][reflectedNum][self.size-1]
                for i in range(self.size-1, 0, -1):  # doesn't include first element
                    self.config[3][reflectedNum][i] = self.config[3][reflectedNum][i-1]
                self.config[3][reflectedNum][0] = last
                last = temp

                self.config[5][0][num] = last

                if (num == 0):
                    self.config[0] = np.rot90(self.config[0], -1)
                elif (num == self.size-1):
                    self.config[2] = np.rot90(self.config[2])
            else:
                #goes through [5,3,4,1]
                last = self.config[5][0][num]
                for i in range(self.size - 1):  # doesn't include first element
                    self.config[5][i][num] = self.config[5][i+1][num]

                temp = self.config[3][reflectedNum][0]
                for i in range(self.size-1):  # doesn't include first element
                    self.config[3][reflectedNum][i] = self.config[3][reflectedNum][i + 1]
                self.config[3][reflectedNum][self.size-1] = last
                last = temp

                temp = self.config[4][self.size-1][num]
                for i in range(self.size-1, 0, -1):  # doesn't include first element
                    self.config[4][i][num] = self.config[4][i-1][num]
                self.config[4][0][num] = last
                last = temp

                temp = self.config[1][reflectedNum][self.size-1]
                for i in range(self.size - 1, 0, -1):  # doesn't include first element
                    self.config[1][reflectedNum][i] = self.config[1][reflectedNum][i - 1]
                self.config[1][reflectedNum][0] = last
                last = temp

                self.config[5][self.size-1][num] = last

                if (num == 0):
                    self.config[0] = np.rot90(self.config[0])
                elif (num == self.size - 1):
                    self.config[2] = np.rot90(self.config[2], -1)
    def __eq__(self, other):
        if (other == None):
            return False
        if (self.size != other.size):
            return False

        for n in range(6):
            for i in range(self.size):
                for j in range(self.size):
                    if (self.config[n][i][j] != other.config[n][i][j]):
                        return False
        return True

    def __hash__(self):
        return hash(str(self.config.data))

    def ifSolved(self)->bool:
        """
        front white, back yellow
        front blue, back green
        front red, back orange
        """
        front = self._checkColor(0)
        if (front == color.noColor):
            return False
        back = self._checkColor(2)
        if (back == color.noColor):
            return False

        indexes = [5,1,4]
        if (front == color.white):
            if (back != color.yellow):
                return False
            middle = [color.green, color.orange, color.blue, color.red]
            mid1 = self._checkColor(3)
            if (mid1 == color.noColor):
                return False

            index = middle.index(mid1)+1

            for i in range(3):
                if (middle[(index+i)%4] != self._checkColor(indexes[i])):
                    return False
            return True

        elif (front == color.yellow):
            if (back != color.white):
                return False
            middle = [color.green, color.red, color.blue, color.orange]
            mid1 = self._checkColor(3)
            if (mid1 == color.noColor):
                return False

            index = middle.index(mid1)+1

            for i in range(3):
                if (middle[(index+i)%4] != self._checkColor(indexes[i])):
                    return False
            return True

        elif (front == color.red):
            if (back != color.orange):
                return False
            middle = [color.blue, color.yellow, color.green, color.white]
            mid1 = self._checkColor(3)
            if (mid1 == color.noColor):
                return False

            index = middle.index(mid1)+1

            for i in range(3):
                if (middle[(index+i)%4] != self._checkColor(indexes[i])):
                    return False
            return True

        elif (front == color.orange):
            if (back != color.red):
                return False
            middle = [color.blue, color.white, color.green, color.yellow]
            mid1 = self._checkColor(3)
            if (mid1 == color.noColor):
                return False

            index = middle.index(mid1)+1

            for i in range(3):
                if (middle[(index+i)%4] != self._checkColor(indexes[i])):
                    return False
            return True

        elif (front == color.blue):
            if (back != color.green):
                return False
            middle = [color.yellow, color.red, color.white, color.orange]
            mid1 = self._checkColor(3)
            if (mid1 == color.noColor):
                return False

            index = middle.index(mid1)+1

            for i in range(3):
                if (middle[(index+i)%4] != self._checkColor(indexes[i])):
                    return False
            return True

        elif (front == color.yellow):
            if (back != color.green):
                return False
            middle = [color.yellow, color.orange, color.white, color.red]
            mid1 = self._checkColor(3)
            if (mid1 == color.noColor):
                return False

            index = middle.index(mid1)+1

            for i in range(3):
                if (middle[(index+i)%4] != self._checkColor(indexes[i])):
                    return False
            return True

        else:
            return False


    def _checkColor(self, n:int)->color:
        color = self.config[n][0][0]
        for i in range(self.size):
            for j in range(self.size):
                if (self.config[n][i][j] != color):
                    return color.noColor
        return color

class RubiksSequence():
    def __init__(self, initialState:Rubiks = None):
        if (initialState == None):
            self.sequence = np.array([])
        else:
            self.sequence = [initialState]
    def add(self, rubiksState:Rubiks)->"RubiksSequence":
        newRubSeq = deepcopy(self)
        newRubSeq.addSelf(rubiksState)
        return newRubSeq
    def addSelf(self, rubiksState:Rubiks)->None:
        self.sequence.append(rubiksState)
    def getLast(self)->Rubiks:
        if (len(self.sequence)):
            return self.sequence[-1]
        return None


class RubiksBFS():
    def __init__(self, initState:Rubiks):
        self.depth:int = 0
        self.size = initState.size
        self.accessedState = {initState: True}
        self.sequences:List[RubiksSequence] = np.array([RubiksSequence(initState)])
        self.solvedSeq = []

    def runBFS(self)->bool:
        while (1):
            if (self._checkSequences()):
                return True
            self.depth += 1

            nextSequence:List[RubiksSequence] = []
            for seq in self.sequences:
                for dir in direction:
                    for n in range(self.size):
                        for bl in [True, False]:
                            last = seq.getLast()
                            nextRub = last.action(dir = dir, num=n, isRev= bl)
                            gt = self.accessedState.get(nextRub)
                            if (gt == None):
                                self.accessedState[nextRub] = True
                                nextSequence.append(seq.add(nextRub))
            if (not len(nextSequence)):
                print("Unsolvable")
                return False


    def _checkSequences(self)->bool:
        self.solvedSeq = []
        for seq in self.sequences:
            rub = seq.getLast()
            if (rub.ifSolved()):
                self.solvedSeq.append(seq)
        return (len(self.solvedSeq))
