# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updownload.ui'
#
# Created: Mon Dec 26 10:35:22 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui,QtNetwork


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
    def run(self, Form):

        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(371, 236)
        Form.setWindowIcon(QtGui.QIcon('car.png'))
        self.ftpClient=QtNetwork.QFtp()
        self.ftpClient.connectToHost(QtCore.QString('192.168.0.4'),port=2121)
        self.ftpClient.login('FTPuser','123')
        self.ftpClient.list()

        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(0, 210, 381, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.uploadButton = QtGui.QPushButton(Form)
        self.uploadButton.setGeometry(QtCore.QRect(0, 180, 81, 31))
        self.uploadButton.setObjectName(_fromUtf8("uploadButton"))
        self.downloadButton = QtGui.QPushButton(Form)
        self.downloadButton.setGeometry(QtCore.QRect(290, 180, 81, 31))
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))

        self.treeWidget = QtGui.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 371, 181))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))

        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 190, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.ftpClient,QtCore.SIGNAL("listInfo(QUrlInfo)"),Form.addToList)
        QtCore.QObject.connect(self.ftpClient,QtCore.SIGNAL("commandFinished(int,bool)"),Form.ftpCommandFinished)
        QtCore.QObject.connect(self.uploadButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.upload_file)
        QtCore.QObject.connect(self.downloadButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.download_file)
        QtCore.QObject.connect(self.ftpClient,QtCore.SIGNAL("dataTransferProgress(qint64,qint64)"),Form.updateDataTransferProgress)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.i=1
        self.filenamels=[]
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "文件上下行", None))
        self.uploadButton.setText(_translate("Form", "上传", None))
        self.downloadButton.setText(_translate("Form", "下载", None))
        self.label.setText(_translate("Form", "中文文件名会乱码！", None))

        self.treeWidget.headerItem().setText(0, _translate("Form", "文件ID", None))
        self.treeWidget.headerItem().setText(1, _translate("Form", "文件名称", None))
        self.treeWidget.headerItem().setText(2, _translate("Form", "文件大小", None))

    def addToList(self,urlInfo):
        self.item = QtGui.QTreeWidgetItem(self.treeWidget)

        self.item.setText(0,QtCore.QString.number(self.i))
        self.i+=1

        filename=str(urlInfo.name()).decode('gbk')

        self.filenamels.append(filename)
        text=_translate("Form",filename, None)
        self.item.setText(1,text)

        size=str(round(float(urlInfo.size())/1024,1))+'KB'
        self.item.setText(2, QtCore.QString(size))


    def upload_file(self):
        filehandle=QtGui.QFileDialog.getOpenFileName(self,self.tr("select a file"),QtCore.QString())
        fileDir = QtCore.QString(filehandle)
        self.remoteFileName=QtCore.QFile(fileDir)
        filename=str(filehandle).split('/')[-1]
        filename=QtCore.QString(filename)
        self.ftpClient.put(self.remoteFileName,filename)
        self.treeWidget.clear()
        self.ftpClient.list()

    def download_file(self):
        fileName =self.treeWidget.currentItem().text(1)
        # print txt
        # fileName,OK = QtGui.QInputDialog.getText(self,"Get File:","Please input file name:",QtGui.QLineEdit.Normal,QtCore.QString())
        if(not fileName.isEmpty()):
            if fileName in self.filenamels:
                self.localFile = QtCore.QFile(fileName)
                self.localFile.open(QtCore.QIODevice.ReadWrite)
                self.ftpClient.get(fileName,self.localFile)

            else:
                QtGui.QMessageBox.question(self, 'Message',"Error filename", QtGui.QMessageBox.Yes)
        else:
            QtGui.QMessageBox.question(self, 'Message',"Empty filename", QtGui.QMessageBox.Yes)

    def ftpCommandFinished(self):
        if (self.ftpClient.currentCommand() == QtNetwork.QFtp.Get):
            print "begin download"
            self.progressBar.setValue(0)
        elif (self.ftpClient.currentCommand()==QtNetwork.QFtp.Put):
            print "begin upload"
            self.progressBar.setValue(0)
        # elif(self.ftpClient.currentCommand()==QtNetwork.QFtp.Close):
        #     print "ftp closed"
        #     self.ftpClient.close()

    def updateDataTransferProgress(self,readByte,totalByte):
        if totalByte >= 4096:
            self.progressBar.setMaximum(totalByte)
            self.progressBar.setValue(readByte)
        else:
            pass

class Ui_show_updownload(QtGui.QWidget,Ui_Form):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.run(self)

