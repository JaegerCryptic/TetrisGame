from PyQt5 import QtCore, QtGui, QtWidgets

class NewWindow(QtWidgets.QMainWindow, object):
        def __init__(self, object):
                super(NewWindow, self).__init__()
                self.initUI(object)
        def initUI(self, object):
                ui = object()
                ui.setupUi(self)


def window(object):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = NewWindow(object)
    win.show()
    sys.exit(app.exec_())

