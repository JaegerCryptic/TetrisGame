from PyQt5 import QtCore, QtGui, QtWidgets
import Startup, Score, Config, Game

class StartWindow(QtWidgets.QMainWindow):
        def __init__(self):
                super(StartWindow, self).__init__()
                self.initUI()
        def initUI(self):
                ui = Startup.Ui
                ui.setupUi(self)

class ConfigtWindow(QtWidgets.QMainWindow):
        def __init__(self):
                super(ConfigtWindow, self).__init__()
                self.initUI()
        def initUI(self):
                ui = Config.Ui
                ui.setupUi(self)

class ScoreWindow(QtWidgets.QMainWindow):
        def __init__(self):
                super(ScoreWindow, self).__init__()
                self.initUI()
        def initUI(self):
                ui = Score.Ui_MainWindow
                ui.setupUi(self)

class GameWindow(QtWidgets.QMainWindow):
        def __init__(self):
                super(GameWindow, self).__init__()
                self.initUI()
        def initUI(self):
                ui = Game.Ui_MainWindow
                ui.setupUi(self)

def window(object):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    strt = StartWindow()
    cofg = ConfigtWindow()
    scr =  ScoreWindow()
    gme = GameWindow()
    widget.addWidget(strt)
    widget.addWidget(scr)
    widget.addWidget(cofg)
    widget.addWidget(gme)
    sys.exit(app.exec_())

