# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DateDialog(QDialog):
    def __init__(self, parent = None):
        super(DateDialog, self).__init__(parent)
        self.setWindowTitle("message")
        self.resize(280,86)

        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)

        buttons.setWindowTitle('Logout')
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        buttons.setGeometry(100, 50, 171, 32)

        label = QLabel(self)
        label.setGeometry(10, 10, 281, 21)
        label.setText("Are you sure to do the operation?")
        label.setFont(QFont("Sim Sun",9,QFont.Bold))


    @staticmethod
    def getDateTime(parent = None):
        dialog = DateDialog(parent)
        result = dialog.exec_()
        return  result == QDialog.Accepted