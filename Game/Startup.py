from PyQt5 import QtCore, QtGui, QtWidgets
import TetrisMain, Score, Config

class Ui(object):
    def exit():
        exit(0)
        
    def setupUi(self, Tetris):
        Tetris.setObjectName("Tetris")
        Tetris.resize(640, 380)
        Tetris.setMinimumSize(QtCore.QSize(640, 380))
        Tetris.setMaximumSize(QtCore.QSize(640, 380))
        Tetris.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        Tetris.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(Tetris)
        self.centralwidget.setMinimumSize(QtCore.QSize(640, 380))
        self.centralwidget.setMaximumSize(QtCore.QSize(640, 380))
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 40, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: red;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 40, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(48)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: orange;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 40, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(48)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: Yellow;\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 40, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(48)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: green;\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 40, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(48)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: purple;\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 40, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(48)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: blue;\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 640, 380))
        self.frame.setMinimumSize(QtCore.QSize(640, 380))
        self.frame.setMaximumSize(QtCore.QSize(640, 380))
        self.frame.setStyleSheet("background: darkblue")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.StartBtn = QtWidgets.QPushButton(self.frame)
        self.StartBtn.setGeometry(QtCore.QRect(0, 200, 641, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.StartBtn.setFont(font)
        self.StartBtn.setMouseTracking(False)
        self.StartBtn.setStyleSheet("border: none;\n"
"color: green;\n"
"\n"
"QPushButton::pressed \n"
"{ \n"
"    color: white;\n"
" }\n"
"\n"
"QPushButton::hover\n"
"{\n"
"     text-decoration: underline; \n"
"    text-decoration-color: green;    \n"
"}")
        self.StartBtn.setCheckable(False)
        self.StartBtn.setObjectName("StartBtn")
        self.ScoreBtn = QtWidgets.QPushButton(self.frame)
        self.ScoreBtn.setGeometry(QtCore.QRect(1, 230, 641, 33))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ScoreBtn.setFont(font)
        self.ScoreBtn.setStyleSheet("border: none;\n"
"color: green;\n"
"QPushButton\n"
"{\n"
"    color: white;\n"
"}")
        self.ScoreBtn.setObjectName("ScoreBtn")
        self.ConfigBtn = QtWidgets.QPushButton(self.frame)
        self.ConfigBtn.setGeometry(QtCore.QRect(0, 270, 641, 33))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ConfigBtn.setFont(font)
        self.ConfigBtn.setStyleSheet("border: none;\n"
"color: green;\n"
"QPushButton\n"
"{\n"
"    color: white;\n"
"}")
        self.ConfigBtn.setObjectName("ConfigBtn")
        self.ConfigBtn.clicked.connect(self.openConfig)
        self.ExitBtn = QtWidgets.QPushButton(self.frame)
        self.ExitBtn.setGeometry(QtCore.QRect(-4, 310, 641, 33))
        self.ExitBtn.clicked.connect(exit)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ExitBtn.setFont(font)
        self.ExitBtn.setStyleSheet("border: none;\n"
"color: green;\n"
"QPushButton\n"
"{\n"
"    color: white;\n"
"}")
        self.ExitBtn.setAutoDefault(False)
        self.ExitBtn.setObjectName("ExitBtn")
        self.StartBtn_2 = QtWidgets.QPushButton(self.frame)
        self.StartBtn_2.setGeometry(QtCore.QRect(0, 0, 111, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.StartBtn_2.setFont(font)
        self.StartBtn_2.setMouseTracking(False)
        self.StartBtn_2.setStyleSheet("border: none;\n"
"color: green;\n"
"\n"
"QPushButton::pressed \n"
"{ \n"
"    color: white;\n"
" }\n"
"\n"
"QPushButton::hover\n"
"{\n"
"     text-decoration: underline; \n"
"    text-decoration-color: green;    \n"
"}")
        self.StartBtn_2.setCheckable(False)
        self.StartBtn_2.setObjectName("StartBtn_2")
        self.StartBtn_3 = QtWidgets.QPushButton(self.frame)
        self.StartBtn_3.setGeometry(QtCore.QRect(0, 20, 111, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.StartBtn_3.setFont(font)
        self.StartBtn_3.setMouseTracking(False)
        self.StartBtn_3.setStyleSheet("border: none;\n"
"color: green;\n"
"\n"
"QPushButton::pressed \n"
"{ \n"
"    color: white;\n"
" }\n"
"\n"
"QPushButton::hover\n"
"{\n"
"     text-decoration: underline; \n"
"    text-decoration-color: green;    \n"
"}")
        self.StartBtn_3.setCheckable(False)
        self.StartBtn_3.setObjectName("StartBtn_3")
        self.frame.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        Tetris.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tetris)
        QtCore.QMetaObject.connectSlotsByName(Tetris)

    def retranslateUi(self, Tetris):
        _translate = QtCore.QCoreApplication.translate
        Tetris.setWindowTitle(_translate("Tetris", "MainWindow"))
        Tetris.setAccessibleName(_translate("Tetris", "Tetris"))
        self.label_2.setText(_translate("Tetris", "T"))
        self.label_3.setText(_translate("Tetris", "e"))
        self.label_4.setText(_translate("Tetris", "t"))
        self.label_5.setText(_translate("Tetris", "r"))
        self.label_6.setText(_translate("Tetris", "s"))
        self.label_7.setText(_translate("Tetris", "i"))
        self.StartBtn.setText(_translate("Tetris", "Start"))
        self.ScoreBtn.setText(_translate("Tetris", "Score"))
        self.ConfigBtn.setText(_translate("Tetris", "Config"))
        self.ExitBtn.setText(_translate("Tetris", "Exit"))
        self.StartBtn_2.setText(_translate("Tetris", "2805ICT 2022"))
        self.StartBtn_3.setText(_translate("Tetris", "Kyle Kent"))

    def openConfig():
        win = TetrisMain.window(Config.Ui)

win = TetrisMain.window(Ui)