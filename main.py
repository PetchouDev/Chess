# coding: utf-8

import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap, QIcon

# creer le widget avec le chessboard à placer dans la fenêtre principale
class Chessboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # creer une grille de 8x8
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        # creer les cases
        for i in range(8):
            for j in range(8):
                # creer une case
                case = QLabel()
                # definir la couleur de la case
                if (i + j) % 2 == 0:
                    case.setStyleSheet("background-color: white")
                else:
                    case.setStyleSheet("background-color: black")
                # ajouter la case à la grille
                self.grid.addWidget(case, i, j)


# creer la fenêtre principale
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


        # afficher la fenêtre principale
        self.show()


    def initUI(self):
        # charger le widget chessboard
        self.chessboard = Chessboard()
        # ajouter le widget chessboard à la fenêtre principale
        self.setCentralWidget(self.chessboard)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
