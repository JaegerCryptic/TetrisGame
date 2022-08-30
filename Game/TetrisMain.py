import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QApplication, QMessageBox
from PyQt5.QtCore import Qt
from random import choice
import copy
import sys
import copy
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import QTimer, Qt
from random import choice


import Block

class StartWindow(QtWidgets.QMainWindow):
        def __init__(self):
                super(StartWindow, self).__init__()
                loadUi("UIFiles//Startup.ui", self)

                self.ConfigBtn.clicked.connect(self.gotoConfig)
                self.ExitBtn.clicked.connect(exit)
                self.ScoreBtn.clicked.connect(self.gotoScore)
                self.StartBtn.clicked.connect(self.gotoGame)

        def gotoConfig(self):
                widget.setCurrentIndex(widget.currentIndex()+2)

        def gotoScore(self):
                widget.setCurrentIndex(widget.currentIndex()+1)

        def gotoGame(self):
                widget.setCurrentIndex(widget.currentIndex()+3)

class ConfigtWindow(QtWidgets.QMainWindow):
        def __init__(self):
                super(ConfigtWindow, self).__init__()
                loadUi("UIFiles//Config.ui", self)

                self.ReturnBtn.clicked.connect(lambda: goBack(self,2))

class ScoreWindow(QtWidgets.QMainWindow):
        def __init__(self):
                super(ScoreWindow, self).__init__()
                loadUi("UIFiles//Score.ui", self)

                self.ReturnBtn.clicked.connect(lambda: goBack(self,1))

class GameWindow(QtWidgets.QMainWindow):
        def __init__(self):
                super(GameWindow, self).__init__()
                loadUi("UIFiles//Game.ui", self)
                
               
                # Initialize Dynamic variables and elements
                self.rows = 10
                self.columns = 10
                self.point_piece = 10
                self.points_line = 100
                self.label = {}
                self.score = 0
                self.lines = 0
                self.board = []
                self.game_running = False

                self.timer = QTimer()
                self.timer.timeout.connect(self.timer_event)
                
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
                                self.label[row, column].setStyleSheet("background-color:lightGrey;border: 1px inset darkGrey")
                                horizontal_board.addWidget(self.label[row, column])
                        vertical_board.addLayout(horizontal_board)
                        vertical_board.setSpacing(0)
                self.setFixedSize(self.size())
                self.start_game()
        
        def start_game(self):
                        # initialization
                        self.score = 0
                        self.lines = 0
                        self.board = []
                        self.init_board()
                        # add first piece to board
                        self.add_new_piece()
                        # display piece on board
                        self.update_piece()
                        # display existing lines on the board
                        self.update_board()
                        # game running is used for Pause, if False=>Pause is active
                        self.game_running = True

                        # set title
                        self.setWindowTitle("Tetris")
                        # set icon
                        self.setWindowIcon(QtGui.QIcon('favicon.png'))

                        # set timer event
                        self.timer = QTimer()
                        self.timer.timeout.connect(self.timer_event)

                        # start game
                        self.start_game()        

        def start_game(self):
                        # initialization
                        self.score = 0
                        self.lines = 0
                        self.board = []
                        self.init_board()
                        # add first piece to board
                        self.add_new_piece()
                        # display piece on board
                        self.update_piece()
                        # display existing lines on the board
                        self.update_board()
                        # game running is used for Pause, if False=>Pause is active
                        self.game_running = True

        def delete_piece(self):
                        # delete piece on board (draw in default color)
                        sheet = "background-color:lightGrey;border: 1px inset darkGrey"
                        origin_rows, origin_columns = self.new_piece.get_origin()
                        for item in self.new_piece.get_relative_positions():
                                self.label[origin_rows+item[0], origin_columns+item[1]].setStyleSheet(sheet)
                        
                
        def update_piece(self):
                        # display piece on board
                        sheet = "background-color:" + self.new_piece.get_color() + ";border: 1px inset darkGrey"
                        origin_rows, origin_columns = self.new_piece.get_origin()
                        for item in self.new_piece.get_relative_positions():
                                self.label[origin_rows+item[0], origin_columns+item[1]].setStyleSheet(sheet)

        def check_move_down(self):
                        self.delete_piece()
                        # check if the piece can move further down
                        if self.new_piece.move_down(self.rows, self.columns, self.board):
                                # if the piece has reached its final position
                                self.add_piece_to_board()
                                self.check_full_lines()
                                self.add_new_piece()
                                self.update_piece()
                                self.update_board()
                                # check when the board is full
                                test_position = copy.deepcopy(self.new_piece.piece)
                                test_position[4][0] += 1
                                if self.new_piece.check_existing_pieces(test_position, self.board) is False:
                                        self.game_over()
                        # otherwise we just update the piece
                        self.update_piece()

        def timer_event(self):
                        if self.game_running is True:
                                self.check_move_down()


        def keyPressEvent(self, event):
                        if event.key() == Qt.Key_Escape:
                                self.close()
                        pressedkey = event.key()
                        if pressedkey == Qt.Key_P:
                                if self.game_running is True:
                                        self.game_running = False
                                else:
                                        self.game_running = True
                                event.accept()
                        if self.game_running is True:
                                if pressedkey == Qt.Key_Up:
                                        self.delete_piece()
                                        self.new_piece.rotate(self.rows, self.columns, self.board)
                                        self.update_piece()
                                        event.accept()
                                elif pressedkey == Qt.Key_Down:
                                        self.check_move_down()
                                        event.accept()
                                elif pressedkey == Qt.Key_Left:
                                        self.delete_piece()
                                        self.new_piece.move_left(self.rows, self.columns, self.board)
                                        self.update_piece()
                                        event.accept()
                                elif pressedkey == Qt.Key_Right:
                                        self.delete_piece()
                                        self.new_piece.move_right(self.rows, self.columns, self.board)
                                        self.update_piece()
                                        event.accept()
                                else:
                                        event.ignore()
        
        def closeEvent(self, event):
            reply = QMessageBox.question(
            self, "Confirm",
            "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No)

            if reply == QMessageBox.Yes:
                goBack(self, 3)
            else:
                event.ignore()    
        
        def add_new_piece(self):
                        # add new piece to board
                        self.score += self.point_piece
                        self.update_statusbar()
                        self.new_piece = Piece()
                
        def init_board(self):
                        for row in range(self.rows):
                                line = [None]*self.columns
                                self.board.append(line)

        def add_piece_to_board(self):
                        # the piece is in its final position and the color of the piece is added to the board
                        origin_rows, origin_columns = self.new_piece.get_origin()
                        for item in self.new_piece.get_relative_positions():
                                self.board[item[0]+origin_rows][item[1]+origin_columns] = self.new_piece.get_color()


        def update_board(self):
                # draw the values of the board
                        for counter_row, row in enumerate(self.board):
                                for counter_column, column in enumerate(row):
                                        if column is not None:
                                                sheet = "background-color:"+column+";border: 1px inset darkGrey"
                                                self.label[counter_row, counter_column].setStyleSheet(sheet)
                                        else:
                                                sheet = "background-color:lightGrey;border: 1px inset darkGrey"
                                                self.label[counter_row, counter_column].setStyleSheet(sheet)

        def check_full_lines(self):
                # a line is full when all the values in the list have a color value (not None)
                        counter_row = self.rows-1
                # we start checking the board from the bottom to the top
                        for row in reversed(self.board):
                                if None not in row:
                                        for i in range(counter_row):
                                                self.board[counter_row-i] = copy.deepcopy(self.board[counter_row-1-i])
                                        self.board[0] = [None]*self.columns
                                        self.check_full_lines()
                                        self.score += self.points_line
                                        self.lines += 1
                                        self.update_statusbar()
                                counter_row -= 1

                
        def update_statusbar(self):
                        speed = int(1000*(1-(self.lines//5/10)))
                        self.message = 'Score:' + str(self.score) + ' Number of lines:'+str(self.lines)
                        self.statusBar().showMessage(self.message)
                        self.timer.start(speed)

        def game_over(self):
                        # stop the game
                        self.game_running = False
                        # create 'Game over' messagebox with score,etc
                        game_over = QMessageBox()
                        game_over.setIcon(QMessageBox.Information)
                        game_over.setText("Game over")
                        game_over.setInformativeText("Score: "+str(self.score)+'\nNumber of lines: '+str(self.lines))
                        game_over.setWindowTitle("Game over")
                        game_over.setStandardButtons(QMessageBox.Ok)
                        game_over.buttonClicked.connect(self.start_game)
                        game_over.exec_()

class Piece:

                def __init__(self):
                        '''
                        T shape
                        long
                        square
                        L right
                        L left
                        S shape
                        Z shape
                        '''
                        shapes = [[[0, -1], [0, 0], [0, 1], [1, 0], [0, 4], 'cyan'],
                                [[0, -1], [0, 0], [0, 1], [0, 2], [0, 4], 'red'],
                                [[0, 0], [0, 1], [1, 0], [1, 1], [0, 4], 'blue'],
                                [[0, -1], [0, 0], [0, 1], [1, 1], [0, 4], 'green'],
                                [[0, -1], [0, 0], [0, 1], [1, -1], [0, 4], 'magenta'],
                                [[0, -1], [0, 0], [1, 0], [1, 1], [0, 4], 'yellow'],
                                [[1, -1], [1, 0], [0, 0], [0, 1], [0, 4], 'black'],
                                ]
                        self.piece = choice(shapes)

                def __str__(self):
                        return 'Positions: {}, {}, {}, {}, Origin: {}, Color: {}'.format(self.piece[0], self.piece[1], self.piece[2], self.piece[3], self.piece[4], self.piece[5])


                def __repr__(self):
                        return 'Piece: '+str(self.piece)

                def move_down(self, rows, columns, board):
                        test_position = copy.deepcopy(self.piece)
                        test_position[4][0] += 1
                        if self.check_position(test_position, rows, columns) and self.check_existing_pieces(test_position, board):
                                self.piece = copy.deepcopy(test_position)
                        else:
                                return True
                
                def move_right(self, rows, columns, board):
                        test_position = copy.deepcopy(self.piece)
                        test_position[4][1] += 1
                        if self.check_position(test_position, rows, columns):
                                if self.check_existing_pieces(test_position, board):
                                        self.piece = copy.deepcopy(test_position)

                def move_left(self, rows, columns, board):
                        test_position = copy.deepcopy(self.piece)
                        test_position[4][1] -= 1
                        if self.check_position(test_position, rows, columns):
                                if self.check_existing_pieces(test_position, board):
                                        self.piece = copy.deepcopy(test_position)

                def rotate(self, rows, columns, board):
                        if self.piece[-1] != 'blue':
                                test_position = copy.deepcopy(self.piece)
                                for item in test_position[:-2]:
                                        item[0], item[1] = item[1], -item[0]
                                if self.check_position(test_position, rows, columns):
                                        if self.check_existing_pieces(test_position, board):
                                                self.piece = copy.deepcopy(test_position)

                def check_position(self, test_position, rows, columns):
                        origin_rows = test_position[-2][0]
                        origin_columns = test_position[-2][1]
                        for item in test_position[:-2]:
                                if origin_columns+item[1] < 0:
                                        return False
                                elif origin_columns+item[1] > columns-1:
                                        return False
                                elif origin_rows+item[0] < 0:
                                        return False
                                elif origin_rows+item[0] > rows-1:
                                        return False
                        return True
                
                def check_existing_pieces(self, test_position, board):
                        origin_rows = test_position[-2][0]
                        origin_columns = test_position[-2][1]
                        for item in test_position[:-2]:
                                if board[origin_rows+item[0]][origin_columns+item[1]] is not None:
                                        return False
                        return True

                def get_origin(self):
                        return self.piece[-2][0], self.piece[-2][1]

                def get_color(self):
                        return self.piece[-1]

                def get_relative_positions(self):
                        return self.piece[:-2]


def goBack(self, index):
        widget.setCurrentIndex(widget.currentIndex()-index)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
strt = StartWindow()
cofg = ConfigtWindow()
scr =  ScoreWindow()
gme = GameWindow()
widget.addWidget(strt)
widget.addWidget(scr)
widget.addWidget(cofg)
widget.addWidget(gme)
widget.show()
sys.exit(app.exec_())
