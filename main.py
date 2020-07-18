from rubiksgui import *

a = QApplication(sys.argv)

w = QMainWindow()
rub = RubiksGui(w, 3)

w.show()
w.setGeometry(200,200,1200,800)
w.setWindowTitle("Rubiks")
w.setCentralWidget(rub)
w.setFixedSize(w.size())

a.exec_()