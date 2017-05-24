# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'learn_plan2.ui'
#
# Created: Fri Nov 25 10:49:01 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


class Ui_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()

        self.resize(398, 100)
        self.setWindowTitle("learnPlan")
        #         buttons = QDialogButtonBox(
        #     QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
        #     Qt.Horizontal, self)
        #
        # buttons.setWindowTitle('Logout')
        # buttons.accepted.connect(self.accept)
        # buttons.rejected.connect(self.reject)
        # buttons.setGeometry(100, 50, 171, 32)
        buttonBox=QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Cancel,
                                     QtCore.Qt.Horizontal,self)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        buttonBox.setGeometry(QtCore.QRect(220, 60, 161, 32))

        global lineEdit
        lineEdit = QtGui.QLineEdit(self)
        lineEdit.setGeometry(QtCore.QRect(10, 10, 371, 51))


    @classmethod
    def learn_plan(cls):
        learnplan = Ui_Dialog()
        result = learnplan.exec_()
        return  result==QtGui.QDialog.Accepted,lineEdit.text()


