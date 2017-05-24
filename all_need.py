# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'all_need.ui'
#
# Created: Wed Nov 30 10:48:34 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form,tup):

        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(520, 331)
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 531, 341))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit.setReadOnly(True)
        for index in range(len(tup)):
            self.textEdit.insertPlainText(_translate("Form", str(tup[index][0])+"|"+str(tup[index][1])+"|"+str(tup[index][2])+"|"+str(tup[index][3])+"\n", None))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "全部需求", None))

class Ui_show_all_need(QtGui.QWidget,Ui_Form):
    def __init__(self,tup):
        QtGui.QWidget.__init__(self)
        self.setupUi(self,tup)