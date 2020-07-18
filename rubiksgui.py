from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import sys
from rubiks import Rubiks
import numpy as np
from typing import List

class RubiksButton(QPushButton):
    def __init__(self, parent:QWidget, num:int, i:int, j:int):
        super().__init__(parent)
        self.faceNum = num
        self.x = i
        self.y = j

class RubiksGui(QWidget):
    def __init__(self, parent:QWidget, n:int):
        super().__init__(parent)
        self.size = n
        self.rubiks = Rubiks(self.size)
        self.buttonGrid:List[List[RubiksButton]] = []
        buttonSize = np.floor(175/n)


        face = [[] for _ in range(6)]
        for i in range(n):
            for j in range(n):
                x = 50+175+buttonSize*i
                y = 50+175+buttonSize*j
                but = RubiksButton(self,0, i, j)
                but.setGeometry(x,y,buttonSize,buttonSize)
                face[i].append(but)
        self.buttonGrid.append(face)

        face = [[] for _ in range(6)]
        for i in range(n):
            for j in range(n):
                x = 50+175+buttonSize*i
                y = 50+2*175+buttonSize*j
                but = RubiksButton(self, 1, i, j)
                but.setGeometry(x,y,buttonSize,buttonSize)
                face[i].append(but)
        self.buttonGrid.append(face)

        face = [[] for _ in range(6)]
        for i in range(n):
            for j in range(n):
                x = 50+175+buttonSize*i
                y = 50+175*3+buttonSize*j
                but = RubiksButton(self, 2, i, j)
                but.setGeometry(x,y,buttonSize,buttonSize)
                face[i].append(but)
        self.buttonGrid.append(face)

        face = [[] for _ in range(6)]
        for i in range(n):
            for j in range(n):
                x = 50+175+buttonSize*i
                y = 50+buttonSize*j
                but = RubiksButton(self, 3, i, j)
                but.setGeometry(x,y,buttonSize,buttonSize)
                face[i].append(but)
        self.buttonGrid.append(face)

        face = [[] for _ in range(6)]
        for i in range(n):
            for j in range(n):
                x = 50+buttonSize*i
                y = 50+175+buttonSize*j
                but = RubiksButton(self, 4, i, j)
                but.setGeometry(x,y,buttonSize,buttonSize)
                face[i].append(but)
        self.buttonGrid.append(face)

        face = [[] for _ in range(6)]
        for i in range(n):
            for j in range(n):
                x = 50+175*2+buttonSize*i
                y = 50+175+buttonSize*j
                but = RubiksButton(self, 5, i, j)
                but.setGeometry(x,y,buttonSize,buttonSize)
                face[i].append(but)
        self.buttonGrid.append(face)

    def rubButtonClicked(self):

        print()
