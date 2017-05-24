# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Tue Nov 08 17:12:18 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys,register,connetmysql
import workpla
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
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(199, 177)
        Form.setWindowIcon(QtGui.QIcon('car.png'))
        Form.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        Form.setFixedSize(Form.width(), Form.height())
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 160, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setMaxLength(11)
        self.horizontalLayout.addWidget(self.lineEdit)
        # global  usermobile
        # usermobile=self.lineEdit.text()
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 50, 160, 51))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(25, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lineEdit_2 = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2.setMaxLength(20)
        # self.lineEdit_2.setStyleSheet("lineedit-password-character: 42")
        self.lineEdit_2.setEchoMode(self.lineEdit_2.Password)
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 100, 160, 51))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.open_registerPage)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.open_workpla)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "测试人员登录", None))
        self.label.setText(_translate("Form", "手机号", None))
        self.label_2.setText(_translate("Form", "密码", None))
        self.pushButton.setText(_translate("Form", "注册", None))
        self.pushButton_2.setText(_translate("Form", "登录", None))

    def open_registerPage(self):
        self.cc=register.Ui_show_register()
        self.cc.show()
    def keyPressEvent(self, event):
        if event.key()==QtCore.Qt.Key_Enter:
            self.open_workpla()
        if event.key()==QtCore.Qt.Key_Return:
            self.open_workpla()
    def open_workpla(self):
        handle,conn=connetmysql.Mysql.connet()
        mobile=self.lineEdit.text()
        tup=connetmysql.Mysql.select_mobi_pas(handle,mobile)
        if tup==():
            QtGui.QMessageBox.question(self, 'Message',"This user does not exist!", QtGui.QMessageBox.Yes)
            return None
        elif self.lineEdit_2.text()!=tup[0][1]:
            QtGui.QMessageBox.question(self, 'Message',"Passwords are not consistent!", QtGui.QMessageBox.Yes)
            return None
        else:
            self.cc=workpla.Ui_show_workpla(self.lineEdit.text())
            self.cc.show()
            self.close()

class Ui_show_login(QtGui.QWidget,Ui_Form):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)



