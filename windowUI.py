import sys

from PyQt4 import  QtGui

from regist import MainWindow
import connetmysql

class Ui(QtGui.QMainWindow, MainWindow.Ui_MainWindow,connetmysql.Mysql):
    def __init__(self):
        super(Ui,self).__init__()
        self.setupUi(self)


app = QtGui.QApplication(sys.argv)
qb = Ui()
qb.show()
sys.exit(app.exec_())