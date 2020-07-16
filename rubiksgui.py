from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import sys
from rubiks import Rubiks
import numpy as np

class RubiksGui(QWidget):
    def __init__(self, parent:QWidget, n:int):
        super().__init__(parent)
        self.size = n
        self.rubiks = Rubiks(self.size)
        self.buttonGrid = []
        buttonSize = np.floor(175/n)


        face = [[] for _ in range(6)]
        for i in range(n):
            for j in range(n):
                x = 50+175+buttonSize*i
                y = 50+175+buttonSize*j
                but = QPushButton(parent=self)
                but.setGeometry(x,y,buttonSize,buttonSize)
                face[i].append(but)
        self.buttonGrid.append(face)

        face = [[] for _ in range(6)]
        for i in range(n):
            for j in range(n):
                x = 50+175+buttonSize*i
                y = 50+2*175+buttonSize*j
                but = QPushButton(parent=self)
                but.setGeometry(x,y,buttonSize,buttonSize)
                face[i].append(but)
        self.buttonGrid.append(face)

        face = [[] for _ in range(6)]
        for i in range(n):
            for j in range(n):
                x = 50+175+buttonSize*i
                y = 50+175*3+buttonSize*j
                but = QPushButton(parent=self)
                but.setGeometry(x,y,buttonSize,buttonSize)
                face[i].append(but)
        self.buttonGrid.append(face)

        face = [[] for _ in range(6)]
        for i in range(n):
            for j in range(n):
                x = 50+175+buttonSize*i
                y = 50+buttonSize*j
                but = QPushButton(parent=self)
                but.setGeometry(x,y,buttonSize,buttonSize)
                face[i].append(but)
        self.buttonGrid.append(face)

        face = [[] for _ in range(6)]
        for i in range(n):
            for j in range(n):
                x = 50+buttonSize*i
                y = 50+175+buttonSize*j
                but = QPushButton(parent=self)
                but.setGeometry(x,y,buttonSize,buttonSize)
                face[i].append(but)
        self.buttonGrid.append(face)

        face = [[] for _ in range(6)]
        for i in range(n):
            for j in range(n):
                x = 50+175*2+buttonSize*i
                y = 50+175+buttonSize*j
                but = QPushButton(parent=self)
                but.setGeometry(x,y,buttonSize,buttonSize)
                face[i].append(but)
        self.buttonGrid.append(face)



a = QApplication(sys.argv)

w = QMainWindow()
rub = RubiksGui(w, 3)

w.show()
w.setGeometry(200,200,1200,800)
w.setWindowTitle("Rubiks")
w.setCentralWidget(rub)
w.setFixedSize(w.size())

a.exec_()