import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt

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
                
                
                Block.Board.InitGame(self)
                
                
                
       
        def keyPressEvent(self, event):
                if event.key() == Qt.Key_Escape:
                        self.close()
        
        def closeEvent(self, event):
            reply = QMessageBox.question(
            self, "Confirm",
            "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No)

            if reply == QMessageBox.Yes:
                goBack(self, 3)
            else:
                event.ignore()    


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
