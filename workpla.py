# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'workpla.ui'
#
# Created: Thu Nov 10 15:28:01 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui,Qt,QtNetwork
import connetmysql,group_fun,login_2
from learn_plan2 import Ui_Dialog
import time
import scoredetail,all_need
import updownload
day=time.strftime('%Y%m%d',time.localtime(time.time()))
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,usermobile):
        global usermobile_1
        usermobile_1=usermobile
        handle,conn=connetmysql.Mysql.connet()
        name=connetmysql.Mysql.select_tester_name(handle,usermobile_1)

        global tester_name
        tester_name=name
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(725, 568)
        MainWindow.setWindowIcon(QtGui.QIcon('car.png'))
        MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 30, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 70, 121, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 30, 41, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setValidator(QtGui.QRegExpValidator(Qt.QRegExp(r"[0-9]+"),self))
        self.lineEdit.setMaxLength(4)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 50, 41, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2.setValidator(QtGui.QRegExpValidator(Qt.QRegExp(r"[0-9]+"),self))
        self.lineEdit_2.setMaxLength(4)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 70, 41, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_3.setValidator(QtGui.QRegExpValidator(Qt.QRegExp(r"[0-9]+"),self))
        self.lineEdit_3.setMaxLength(4)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 90, 41, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 30, 41, 20))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(220, 50, 41, 20))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(220, 70, 41, 20))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        tup=connetmysql.Mysql.select_need(handle,tester_name)


        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 200, 725, 292))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,360)
        self.tableWidget.setColumnWidth(2,65)
        self.tableWidget.setColumnWidth(3,85)
        self.tableWidget.setColumnWidth(4,100)
        self.tableWidget.setRowCount(len(tup)+1)
        for index in range(len(tup)+1):
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(index, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setUnderline(False)
        item.setFont(font)


        for index in range(len(tup)+1):
            item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(index, 0, item)
            item = QtGui.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(index, 1, item)
            item = QtGui.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(index, 2, item)
            item = QtGui.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(index, 3, item)
            item = QtGui.QTableWidgetItem()

            self.tableWidget.setItem(index, 4, item)
            item = QtGui.QTableWidgetItem()

        for index in range(len(tup)):
            item = self.tableWidget.verticalHeaderItem(index)
            item.setText(_translate("MainWindow", "第"+str(index+1)+"行", None))
        self.tableWidget.verticalHeaderItem(len(tup))


        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        for index in range(len(tup)):
            item = self.tableWidget.item(index, 0)
            item.setText(_translate("MainWindow",str(tup[index][0]), None))

            self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
            self.textBrowser.setReadOnly(True)
            self.textBrowser.setOpenExternalLinks(True)
            self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
            self.tableWidget.setCellWidget(index,1,self.textBrowser)
            self.textBrowser.setHtml(_translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\"></style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\"><a href=\""+str(tup[index][4])+"\"><span style=\" text-decoration: underline;\">"+str(tup[index][1])+"</span></a></body></html>", None))

            item = self.tableWidget.item(index, 2)
            item.setText(_translate("MainWindow",str(tup[index][2]), None))
            item = self.tableWidget.item(index, 3)
            item.setText(_translate("MainWindow",str(tup[index][3]), None))
            item = self.tableWidget.item(index, 4)

            item.setText(_translate("MainWindow",str(tup[index][5]), None))


        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.tableWidget.setCellWidget(len(tup),4,self.pushButton_8)

        self.pushButton_9 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.tableWidget.setCellWidget(len(tup),3,self.pushButton_9)

        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 10, 31, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 10, 31, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 10, 54, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_9 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(300, 70, 41, 20))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_8 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(300, 50, 41, 20))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_7 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(300, 30, 41, 20))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.textEdit_3 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 490, 725, 40))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 54, 23))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 0, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(460, 10, 54, 12))
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_10 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(660, 30, 41, 20))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(660, 10, 54, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(520, 10, 91, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))

        self.lineEdit_11 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(590, 30, 61, 20))
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_12 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(590, 50, 61, 20))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.lineEdit_13 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(590, 70, 61, 20))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(530, 35, 54, 12))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(530, 55, 54, 12))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(530, 75, 54, 12))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(530, 95, 54, 12))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lineEdit_14 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(590, 90, 61, 20))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.lineEdit_15 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(660, 50, 41, 20))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.lineEdit_16 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(660, 70, 41, 20))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.lineEdit_17 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(660, 90, 41, 20))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(600, 10, 54, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.lineEdit_18 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_18.setGeometry(QtCore.QRect(360, 30, 51, 20))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(0, 104, 51, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.textEdit_4 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(0, 130, 451, 61))
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))

        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 190, 725, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(360, 10, 61, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 100, 41, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(360, 50, 52, 23))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 725, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuLogout = QtGui.QMenu(self.menubar)
        self.menuLogout.setObjectName(_fromUtf8("menuLogout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionLogout = QtGui.QAction(MainWindow)
        self.actionLogout.setObjectName(_fromUtf8("actionLogout"))
        self.menuLogout.addAction(self.actionLogout)
        self.menubar.addAction(self.menuLogout.menuAction())

        self.push_appendix = QtGui.QPushButton(self.centralwidget)
        self.push_appendix.setGeometry(QtCore.QRect(450, 170, 75, 23))
        self.push_appendix.setObjectName(_fromUtf8("push_appendix"))




        self.retranslateUi(MainWindow,usermobile)
        self.init_data()
        self.init_tester_data()
        self.push_plan_sql()


        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.push_sql)
        QtCore.QObject.connect(self.push_appendix, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.open_fujian)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")),MainWindow.open_plan)

        QtCore.QObject.connect(self.menubar, QtCore.SIGNAL(_fromUtf8("triggered(QAction*)")), MainWindow.logout)

        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.commit_need)
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.list_need)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.score_detial)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        connetmysql.Mysql.close(handle,conn)

    def retranslateUi(self, MainWindow,usermobile):
        handle,conn=connetmysql.Mysql.connet()
        tup=connetmysql.Mysql.select_duty(handle,usermobile_1)
        strtitle="Active user:"+str(usermobile[0:4])+"****"+str(usermobile[8:11])+"  责任模块:"+str(tup)
        MainWindow.setWindowTitle(_translate("MainWindow",strtitle, None))
        self.label.setText(_translate("MainWindow", "提交bug数量", None))
        self.label_2.setText(_translate("MainWindow", "新增用例数量", None))
        self.label_3.setText(_translate("MainWindow", "反馈线上问题数量", None))
        self.pushButton.setText(_translate("MainWindow", "提交", None))
        self.menuLogout.setTitle(_translate("MainWindow", "菜单", None))
        self.actionLogout.setText(_translate("MainWindow", "登出", None))


        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "需求ID", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "需求名称", None))

        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "需求状态", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "需求时间", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "测试状态(可编辑)", None))

        self.label_4.setText(_translate("MainWindow", "今日", None))
        self.label_5.setText(_translate("MainWindow", "当月", None))
        self.label_6.setText(_translate("MainWindow", "历史统计", None))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">每日/周必做：用例关联需求、bug关联计划、工时、周报、兼容性测试、okr测试、接口测试、监控开发自测、说明内测通过、描述公测流程！</span></p></body></html>", None))
        self.label_7.setText(_translate("MainWindow", "当前日期", None))
        self.pushButton_3.setText(_translate("MainWindow",day, None))
        self.label_9.setText(_translate("MainWindow", "加减分", None))
        self.label_10.setText(_translate("MainWindow", "其余成员数据", None))

        self.pushButton_8.setText(_translate("MainWindow", "提交", None))
        self.pushButton_9.setText(_translate("MainWindow", "所有需求", None))

        tup=connetmysql.Mysql.init_user_data(handle,usermobile_1)

        connetmysql.Mysql.close(handle,conn)
        namelist=group_fun.init_compute_user(tup,flag=True)

        if len(namelist)==1:
            self.label_11.setText(_translate("MainWindow", namelist[0], None))
        elif len(namelist)==2:
            self.label_11.setText(_translate("MainWindow", namelist[0], None))
            self.label_12.setText(_translate("MainWindow", namelist[1], None))
        elif len(namelist)==3:
            self.label_11.setText(_translate("MainWindow", namelist[0], None))
            self.label_12.setText(_translate("MainWindow", namelist[1], None))
            self.label_13.setText(_translate("MainWindow", namelist[2], None))
        elif len(namelist)==4:
            self.label_11.setText(_translate("MainWindow", namelist[0], None))
            self.label_12.setText(_translate("MainWindow", namelist[1], None))
            self.label_13.setText(_translate("MainWindow", namelist[2], None))
            self.label_14.setText(_translate("MainWindow", namelist[3], None))
        self.label_15.setText(_translate("MainWindow", "历史统计", None))
        self.label_16.setText(_translate("MainWindow", "学习计划", None))
        self.label_17.setText(_translate("MainWindow", "加减分统计", None))
        self.pushButton_5.setText(_translate("MainWindow", "定制", None))
        self.pushButton_7.setText(_translate("MainWindow", "分数详情", None))
        self.push_appendix.setText(_translate("MainWindow", "附件上下行", None))


    def init_data(self):
        handle,conn=connetmysql.Mysql.connet()
        tup_mouth,tup_all=connetmysql.Mysql.init_data(handle,usermobile_1,day)

        bug,case,gub=group_fun.init_compute(tup_mouth=tup_mouth,tup_all=None)
        self.lineEdit_4.setText(bug)
        self.lineEdit_5.setText(case)
        self.lineEdit_6.setText(gub)

        bug,case,gub,score=group_fun.init_compute(tup_mouth=None,tup_all=tup_all)
        self.lineEdit_7.setText(bug)
        self.lineEdit_8.setText(case)
        self.lineEdit_9.setText(gub)
        self.lineEdit_18.setText(score)

        connetmysql.Mysql.close(handle,conn)




    def init_tester_data(self):
        handle,conn=connetmysql.Mysql.connet()
        tup=connetmysql.Mysql.init_user_data(handle,usermobile_1)
        connetmysql.Mysql.close(handle,conn)
        buglist,caselist,gublist,scorelist=group_fun.init_compute_user(tup,flag=False)
        if len(buglist)==1:
            self.lineEdit_10.setText(str(scorelist[0]))
            self.lineEdit_11.setText(str(buglist[0])+','+str(caselist[0])+','+str(gublist[0]))
        elif len(scorelist)==2:
            self.lineEdit_10.setText(str(scorelist[0]))
            self.lineEdit_11.setText(str(buglist[0])+','+str(caselist[0])+','+str(gublist[0]))
            self.lineEdit_15.setText(str(scorelist[1]))
            self.lineEdit_12.setText(str(buglist[1])+','+str(caselist[1])+','+str(gublist[1]))
        elif len(scorelist)==3:
            self.lineEdit_10.setText(str(scorelist[0]))
            self.lineEdit_15.setText(str(scorelist[1]))
            self.lineEdit_16.setText(str(scorelist[2]))
            self.lineEdit_11.setText(str(buglist[0])+','+str(caselist[0])+','+str(gublist[0]))
            self.lineEdit_12.setText(str(buglist[1])+','+str(caselist[1])+','+str(gublist[1]))
            self.lineEdit_13.setText(str(buglist[2])+','+str(caselist[2])+','+str(gublist[2]))
        elif len(scorelist)==4:
            self.lineEdit_10.setText(str(scorelist[0]))
            self.lineEdit_15.setText(str(scorelist[1]))
            self.lineEdit_16.setText(str(scorelist[2]))
            self.lineEdit_17.setText(str(scorelist[3]))
            self.lineEdit_11.setText(str(buglist[0])+','+str(caselist[0])+','+str(gublist[0]))
            self.lineEdit_12.setText(str(buglist[1])+','+str(caselist[1])+','+str(gublist[1]))
            self.lineEdit_13.setText(str(buglist[2])+','+str(caselist[2])+','+str(gublist[2]))
            self.lineEdit_14.setText(str(buglist[3])+','+str(caselist[3])+','+str(gublist[3]))

    def push_sql(self):
        handle,conn=connetmysql.Mysql.connet()
        if connetmysql.Mysql.insert_worknumber(handle,self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text(),usermobile_1,day):
            QtGui.QMessageBox.question(self, 'Message',"Today has been submitted!", QtGui.QMessageBox.Yes)
            return None
        else:
            connetmysql.Mysql.close(handle,conn)
            QtGui.QMessageBox.question(self, 'Message',"Commit success!", QtGui.QMessageBox.Yes)
            self.init_data()

    def open_fujian(self):
        self.cc=updownload.Ui_show_updownload()
        self.cc.start()


    def open_plan(self):

        result,content=Ui_Dialog.learn_plan()
        if result:
            handle,conn=connetmysql.Mysql.connet()
            connetmysql.Mysql.insert_learn_plan(handle,content,usermobile_1)
            QtGui.QMessageBox.question(self, 'Message',"Plan success!", QtGui.QMessageBox.Yes)
            self.push_plan_sql()
        else:
            pass


    def push_plan_sql(self):
        handle,conn=connetmysql.Mysql.connet()
        tup=connetmysql.Mysql.select_learn_plan(handle,usermobile_1)
        if len(tup)==2:
            self.textEdit_4.setText(_translate(None,str(tup[0][0]), None)+'\n'+_translate(None,str(tup[1][0]), None))
        elif len(tup)==1:
            self.textEdit_4.setText(_translate(None,str(tup[0][0]), None))
        connetmysql.Mysql.close(handle,conn)

    def closeEvent1(self, event):
        pass

    def logout(self):
        reply = QtGui.QMessageBox.question(self, 'Message',
        "Are you sure to logout?", QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self.cc=login_2.Ui_show_login()
            self.cc.show()
            self.close()
        else:
            pass
    def score_detial(self):
        handle,conn=connetmysql.Mysql.connet()
        tup=connetmysql.Mysql.select_score_reason(handle,usermobile_1)
        self.cc=scoredetail.Ui_show_scoreDetail(tup)
        self.cc.show()
        connetmysql.Mysql.close(handle,conn)

    def commit_need(self):
        idls,endls=[],[]
        handle,conn=connetmysql.Mysql.connet()
        try:
            rows=self.tableWidget.rowCount()
            for index in range(rows):
                idls.append(self.tableWidget.item(index,0).text())
                endls.append(self.tableWidget.item(index,4).text())
        except:
            QtGui.QMessageBox.question(self, 'Message',"State error!", QtGui.QMessageBox.Yes)
            return None

        connetmysql.Mysql.update_need(handle,idls,endls)
        connetmysql.Mysql.close(handle,conn)
        QtGui.QMessageBox.question(self, 'Message',"Submit successfully!", QtGui.QMessageBox.Yes)

    def list_need(self):
        handle,conn=connetmysql.Mysql.connet()
        tup=connetmysql.Mysql.select_all_need(handle,tester_name)
        connetmysql.Mysql.close(handle,conn)
        self.cc=all_need.Ui_show_all_need(tup)
        self.cc.show()





class Ui_show_workpla(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,usermobile):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self,usermobile)