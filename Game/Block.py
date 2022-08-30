import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import QTimer, Qt
from random import choice



class Board:
    def InitGame(object):
        object.rows = 12
        object.columns = 13
        object.point_piece = 10
        object.points_line = 100
        object.label = {}
        object.score = 0
        object.lines = 0
        object.board = []
        object.game_running = False
        
        horizontal_layout = QHBoxLayout(object.Board)
        horizontal_layout.setSpacing(20)

        vertical_board = QVBoxLayout()
        horizontal_layout.addLayout(vertical_board)
        for row in range(0, object.rows):
                horizontal_board = QHBoxLayout()
                horizontal_board.setSpacing(0)
                for column in range(0, object.columns):
                    object.label[row, column] = QLabel(object)
                    object.label[row, column].setFixedHeight(40)
                    object.label[row, column].setFixedWidth(40)
                    object.label[row, column].setStyleSheet("background-color:lightGrey;border: 1px inset darkGrey")
                    horizontal_board.addWidget(object.label[row, column])
                vertical_board.addLayout(horizontal_board)
                vertical_board.setSpacing(0)


class Shape:
    Empty = 0
    Z = 1
    S = 2
    Line = 3
    T = 4
    Square = 5
    L = 6
    Mirror = 7




class Block:
    blockCoords = (
        ((0, 0), (0, 0), (0, 0), (0, 0)),
        ((0, -1), (0, 0), (-1, 0), (-1, 1)),
        ((0, -1), (0, 0), (1, 0), (1, 1)),
        ((0, -1), (0, 0), (0, 1), (0, 2)),
        ((-1, 0), (0, 0), (1, 0), (0, 1)),
        ((0, 0), (1, 0), (0, 1), (1, 1)),
        ((-1, -1), (0, -1), (0, 0), (0, 1)),
        ((1, -1), (0, -1), (0, 0), (0, 1))
    )