import copy
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import QTimer, Qt
from random import choice

class GameBoard:
    def initGame(self):
        self.rows = 12
        self.columns = 13
        self.point_shape = 10
        self.points_line = 100
        self.label = {}
        self.score = 0
        self.lines = 0
        self.board = []
        self.game_running = False
        
        # Attach to widget Board from UIFiles Game.ui
        horizontal_layout = QHBoxLayout(self.Board)
        horizontal_layout.setSpacing(20)

        vertical_board = QVBoxLayout()
        horizontal_layout.addLayout(vertical_board)
        for row in range(0, self.rows):
                horizontal_board = QHBoxLayout()
                horizontal_board.setSpacing(0)
                for column in range(0, self.columns):
                    self.label[row, column] = QLabel(self)
                    self.label[row, column].setFixedHeight(40)
                    self.label[row, column].setFixedWidth(40)
                    self.label[row, column].setStyleSheet("background-color:darkblue")
                    horizontal_board.addWidget(self.label[row, column])
                vertical_board.addLayout(horizontal_board)
                vertical_board.setSpacing(0)
        
        # set counter
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: GameBoard.counter_event(self))

        #Initialze board rows and columns
        for row in range(self.rows):
            line = [None]*self.columns
            self.board.append(line)
        # Add shape to board
        GameBoard.newShape(self)
        # Display shape to board
        GameBoard.displayShape(self)
        self.game_running = True

    # Add shape to screen
    def newShape(self):
        self.new_shape = Shape()
        GameBoard.updateStatus(self)

    def updateStatus(self):
        speed = int(1000*(1-(self.lines//5/10)))
        self.timer.start(speed)

    # Display shape to board
    def displayShape(self):
        sheet = "background-color:" + self.new_shape.getColor() + ";border: 1px inset blue"
        start_rows, start_columns = self.new_shape.getStart()
        for item in self.new_shape.getPosition():
            self.label[start_rows+item[0], start_columns+item[1]].setStyleSheet(sheet)

    # Delete shape on board
    def deleteShape(self): 
        sheet = "background-color:darkblue;"
        start_rows, start_columns = self.new_shape.getStart()
        for item in self.new_shape.getPosition():
            self.label[start_rows+item[0], start_columns+item[1]].setStyleSheet(sheet)

    def keyPressEvent(self, event):
        if self.game_running is True:
            if event.key() == Qt.Key_W:
                GameBoard.deleteShape(self)
                self.new_shape.rotate(self.rows, self.columns, self.board)
                GameBoard.displayShape(self)
                event.accept()
            elif event.key() == Qt.Key_A:
                GameBoard.deleteShape(self)
                self.new_shape.moveLeft(self.rows, self.columns, self.board)
                GameBoard.displayShape(self)
                event.accept()
            elif event.key() == Qt.Key_D:
                GameBoard.deleteShape(self)
                self.new_shape.moveRight(self.rows, self.columns, self.board)
                GameBoard.displayShape(self)
                event.accept()
            else:
                event.ignore()

    def checkDownMove(self):
        GameBoard.deleteShape(self)
        # check if shape can move further down
        if self.new_shape.moveDown(self.rows, self.columns, self.board):
            # if shape at bottom
            GameBoard.setShapeToBoard(self)
            GameBoard.newShape(self)
            GameBoard.displayShape(self)
            GameBoard.refreshBoard(self)
        GameBoard.displayShape(self)

    def refreshBoard(self):
        # draw the values of the board
        for counter_row, row in enumerate(self.board):
            for counter_column, column in enumerate(row):
                if column is not None:
                    sheet = "background-color:"+column+";border: 1px inset blue"
                    self.label[counter_row, counter_column].setStyleSheet(sheet)
                else:
                    sheet = "background-color:darkblue"
                    self.label[counter_row, counter_column].setStyleSheet(sheet)
    
    def counter_event(self):
        if self.game_running is True:
            GameBoard.checkDownMove(self)

    def setShapeToBoard(self):
        # set shape to the board
        start_rows, start_columns = self.new_shape.getStart()
        for item in self.new_shape.getPosition():
            self.board[item[0]+start_rows][item[1]+start_columns] = self.new_shape.getColor()
class Shape:
    def __init__(self):
        '''
        line
        L left
        L right
        square
        S
        T
        Z
        '''
        shapes = [[[0, -1], [0, 0], [0, 1], [0, 2], [0, 4], 'white'],
                  [[0, -1], [0, 0], [0, 1], [-1, -1], [1, 4], 'purple'],
                  [[0, -1], [0, 0], [0, 1], [-1, 1], [1, 4], 'orange'],
                  [[0, 0], [0, 1], [1, 0], [1, 1], [0, 4], 'yellow'],
                  [[0, 1], [0, 0], [1, 0], [1, -1], [0, 4], 'green'],
                  [[0, -1], [0, 0], [0, 1], [-1, 0], [1, 4], 'blue'],
                  [[1, 1], [1, 0], [0, 0], [0, -1], [0, 4], 'red'],
                 ]
        self.shape = choice(shapes)

    def __str__(self):
        return 'Positions: {}, {}, {}, {}, Start: {}, Color: {}'.format(self.shape[0], self.shape[1], self.shape[2], self.shape[3], self.shape[4], self.shape[5])

    def __repr__(self):
        return 'Shape: '+str(self.shape)

    def getStart(self):
        return self.shape[-2][0], self.shape[-2][1]

    def getColor(self):
        return self.shape[-1]
    
    def getPosition(self):
        return self.shape[:-2]

    def moveDown(self, rows, columns, board):
        tmp_pos = copy.deepcopy(self.shape)
        tmp_pos[4][0] += 1
        if self.checkPosition(tmp_pos, rows, columns) and self.checkExistingShapes(tmp_pos, board):
                self.shape = copy.deepcopy(tmp_pos)
        else:
            return True

    def checkPosition(self, tmp_pos, rows, columns):
        start_rows = tmp_pos[-2][0]
        start_columns = tmp_pos[-2][1]
        for item in tmp_pos[:-2]:
            if start_columns+item[1] < 0:
                return False
            elif start_columns+item[1] > columns-1:
                return False
            elif start_rows+item[0] < 0:
                return False
            elif start_rows+item[0] > rows-1:
                return False
        return True

    def checkExistingShapes(self, tmp_pos, board):
        start_rows = tmp_pos[-2][0]
        start_columns = tmp_pos[-2][1]
        for item in tmp_pos[:-2]:
            if board[start_rows+item[0]][start_columns+item[1]] is not None:
                return False
        return True

    def rotate(self, rows, columns, board):
        if self.shape[-1] != 'blue':
            tmp_position = copy.deepcopy(self.shape)
            for item in tmp_position[:-2]:
                item[0], item[1] = item[1], -item[0]
            if self.checkPosition(tmp_position, rows, columns):
                if self.checkExistingShapes(tmp_position, board):
                    self.shape = copy.deepcopy(tmp_position)

    def moveRight(self, rows, columns, board):
        tmp_position = copy.deepcopy(self.shape)
        tmp_position[4][1] += 1
        if self.checkPosition(tmp_position, rows, columns):
            if self.checkExistingShapes(tmp_position, board):
                self.shape = copy.deepcopy(tmp_position)

    def moveDown(self, rows, columns, board):
        tmp_position = copy.deepcopy(self.shape)
        tmp_position[4][0] += 1
        if self.checkPosition(tmp_position, rows, columns) and self.checkExistingShapes(tmp_position, board):
                self.shape = copy.deepcopy(tmp_position)
        else:
            return True

    def moveLeft(self, rows, columns, board):
        tmp_position = copy.deepcopy(self.shape)
        tmp_position[4][1] -= 1
        if self.checkPosition(tmp_position, rows, columns):
            if self.checkExistingShapes(tmp_position, board):
                self.shape = copy.deepcopy(tmp_position)





