# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created: Tue Nov 08 17:40:58 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import connetmysql,re,workpla

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
        Form.resize(227, 183)
        Form.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        Form.setFixedSize(Form.width(), Form.height())
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 140, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 181, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setMaxLength(11)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 40, 181, 31))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lineEdit_2 = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2.setMaxLength(15)
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 70, 181, 31))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem1 = QtGui.QSpacerItem(17, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lineEdit_3 = QtGui.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_3.setMaxLength(20)
        self.lineEdit_3.setEchoMode(self.lineEdit_3.Password)
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 100, 181, 31))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_4 = QtGui.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_4.setMaxLength(20)
        self.lineEdit_4.setEchoMode(self.lineEdit_4.Password)
        self.horizontalLayout_4.addWidget(self.lineEdit_4)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.regisert_sql)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "测试人员注册", None))
        self.pushButton.setText(_translate("Form", "确认注册", None))
        self.label.setText(_translate("Form", "新手机号", None))
        self.label_2.setText(_translate("Form", "姓名", None))
        self.label_3.setText(_translate("Form", "新密码", None))
        self.label_4.setText(_translate("Form", "重复密码", None))

    def regisert_sql(self):
        handle,conn=connetmysql.Mysql.connet()
        tup=connetmysql.Mysql.select_user(handle)
        tup2=connetmysql.Mysql.select_all_user(handle)
        p2 = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
        phonematch = p2.match(self.lineEdit.text())
        print tup2
        if tup2>=5:
            QtGui.QMessageBox.question(self, 'Message',"Registration number is full!", QtGui.QMessageBox.Yes)
            return None
        else:
            pass
        if phonematch:
            pass
        else:
            QtGui.QMessageBox.question(self, 'Message',"error phone number!", QtGui.QMessageBox.Yes)
            return None

        if  self.lineEdit.text() and self.lineEdit_2.text() and self.lineEdit_3.text() and self.lineEdit_4.text()!=None:
            pass
        else:
            QtGui.QMessageBox.question(self, 'Message',"Edit box cannot be empty!", QtGui.QMessageBox.Yes)
            return None

        if self.lineEdit_3.text()==self.lineEdit_4.text():
            pass
        else:
            QtGui.QMessageBox.question(self, 'Message',"Passwords are not consistent!", QtGui.QMessageBox.Yes)
            return None

        if (str(self.lineEdit.text()),) in tup:
            QtGui.QMessageBox.question(self, 'Message',"Cell phone number already exists", QtGui.QMessageBox.Yes)
        else:
            connetmysql.Mysql.inster(handle,self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text())
            connetmysql.Mysql.close(handle,conn)
            reply=QtGui.QMessageBox.question(self, 'Message',"Congratulations!", QtGui.QMessageBox.Yes)
            if reply == QtGui.QMessageBox.Yes:
                self.close()
            self.cc=workpla.Ui_show_workpla(self.lineEdit.text())
            self.cc.show()



class Ui_show_register(QtGui.QWidget,Ui_Form):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)