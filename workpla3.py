#coding:utf-8
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtNetwork import *


import sys
reload(sys)
sys.setdefaultencoding("utf-8")
class FtpClient(QWidget):
    def __init__(self,parent=None):
        super(FtpClient,self).__init__(parent)
        self.setWindowTitle(u"FTP Client")
        # self.fileVewer = FileDir()
        self.connect(self.fileVewer,SIGNAL("iamsure"),self.locate)
        
        self.currentPath = QString()
        self.labelServer =QLabel()
        self.labelServer.setText(u"服务器地址")
        self.lineEditServer = QLineEdit()
        self.lineEditServer.setText(u"192.168.0.4")
        self.lineEditServer.setContextMenuPolicy(Qt.NoContextMenu)#去掉默认的右键菜单

        self.labelUser = QLabel()
        self.labelUser.setText(u"用户名")
        
        self.lineEditUser = QLineEdit()
        self.lineEditUser.setText(u"FTPuser")
        
        self.labelPassword = QLabel()
        self.labelPassword.setText(u"密码:")
        
        self.lineEditPassword = QLineEdit()
        self.lineEditPassword.setText(u"123")
            
        self.pushButtonLogin = QPushButton()
        self.pushButtonLogin.setText(u"登录" ) 
        
        self.pushButtonPut = QPushButton()
        self.pushButtonPut.setText( u"上传" )
        
        self.pushButtonGet = QPushButton()
        self.pushButtonGet.setText(u"下载" )
        
        self.treeWidget = QTreeWidget()
        self.treeWidget.setColumnCount(5)
        
        self.pbar = QProgressBar()
        self.pbar.setValue(0)

        
        gLayout = QGridLayout()
        gLayout.addWidget( self.labelServer,0,0 )
        gLayout.addWidget( self.lineEditServer,0,1 )
        gLayout.addWidget( self.labelUser,1,0 )
        gLayout.addWidget( self.lineEditUser,1,1 )
        gLayout.addWidget( self.labelPassword,2,0 )
        gLayout.addWidget( self.lineEditPassword,2,1 )
        
        hbLayout = QHBoxLayout()
        hbLayout.addWidget( self.pushButtonPut )
        hbLayout.addWidget( self.pushButtonGet )

        vbLayout = QVBoxLayout()
        vbLayout.addLayout( gLayout )
        vbLayout.addWidget( self.pushButtonLogin )
        vbLayout.addLayout( hbLayout )
        vbLayout.addWidget(self.pbar)
        # vbLayout.addLayout(hbLayout1)
        vbLayout.addWidget(self.treeWidget)
        
        self.setLayout(vbLayout)
    
        self.connect(self.pushButtonLogin,SIGNAL("clicked()"),self.slotLogin)
        self.connect(self.pushButtonPut,SIGNAL("clicked()"),self.slotPut)
        self.connect(self.pushButtonGet,SIGNAL("clicked()"),self.slotGet)
        
        self.pushButtonPut.setEnabled(False)
        self.pushButtonGet.setEnabled(False)

        self.curStatus=''
        # self.delStatus=''
        self.delList = []

    def slotLogin(self):
        serverAddress = QString(self.lineEditServer.text())
        if(serverAddress.isEmpty()):
            QMessageBox.warning(self,u"error",u"Please input server address!")
            return
        userName = QString(self.lineEditUser.text())
        if(userName.isEmpty()):
            QMessageBox.warning(self,u"error",u"Please input user name!")
            return
        password = QString(self.lineEditPassword.text())
        self.ftpClient = QFtp()
        self.ftpClient.connectToHost(serverAddress,port=2121)
        self.ftpClient.login(userName,password)
    
    
        self.treeWidget.clear()
        self.cucurrentPath = QString()
        # self.isDirectory = {}

        self.connect(self.ftpClient,SIGNAL("commandFinished(int,bool)"),self.ftpCommandFinished)
        self.connect(self.ftpClient,SIGNAL("listInfo(QUrlInfo)"),self.addToList)
        self.connect(self.ftpClient,SIGNAL("dataTransferProgress(qint64,qint64)"),self.updateDataTransferProgress)

    def ftpCommandFinished(self):
        if (self.ftpClient.currentCommand() == QFtp.Login):
            print "login success"
            self.pushButtonPut.setEnabled(True)
            self.pushButtonGet.setEnabled(True)
            self.ftpClient.list()   #发射listInfo()信号，显示文件列表
    
        elif (self.ftpClient.currentCommand() == QFtp.Get):
            print "begin download"
            self.pbar.setValue(0)
        elif (self.ftpClient.currentCommand()==QFtp.Put):
            print "begin upload"
            self.pbar.setValue(0)
    
        elif (self.ftpClient.currentCommand() == QFtp.Close):
            print "disconnected"

    def addToList(self,urlInfo):

        name = str(urlInfo.name())
        print name.decode('gbk')

        item = QTreeWidgetItem(self.treeWidget)

        item.setText(1, urlInfo.name())
        item.setText(2, QString.number(urlInfo.size()))
        item.setText(3, urlInfo.owner())
        item.setText(4, urlInfo.group())
        item.setText(4, urlInfo.lastModified().toString('MMM dd yyyy'))

        if (not self.treeWidget.currentItem()):
            self.treeWidget.setCurrentItem(self.treeWidget.topLevelItem(0))
            self.treeWidget.setEnabled(True)

    def updateDataTransferProgress(self,readByte,totalByte):
        if totalByte >= 4096:
            self.pbar.setMaximum(totalByte)
            self.pbar.setValue(readByte)
        else:
            pass


    def locate(self,dir,noydir):
        fileDir = QString(dir)

        if self.curStatus == 'PUT':
            if noydir == 'file':
                fileName,ok= QInputDialog.getText(self, u"Put File1:",u"Please input file name:", QLineEdit.Normal, QString())
                # print fileName,ok
                if(ok and not fileName.isEmpty()):
                    self.remoteFileName=QFile(fileDir)
                    if not self.remoteFileName.open(QIODevice.ReadWrite):
                        del self.remoteFileName
                    print self.remoteFileName, fileName
                    self.ftpClient.put(self.remoteFileName, fileName)
                self.ftpClient.list()
            else:
                QMessageBox.information(self, u'提示',u'请选择文件')
        else:
            filedir = QString()
            if noydir == 'file':
                dirf = dir.split('/')
                for i in range(len(dirf)-1):
                    filedir += dirf[i]+'/'
            else:
                filedir = dir+'/'
            fileName,ok= QInputDialog.getText(self, u"Put File2:",u"Please input file name:", QLineEdit.Normal, QString())
            if(ok and not fileName.isEmpty()):
                fileDir = filedir + fileName    
                fileName = self.treeWidget.currentItem().text(1)
                self.localFile= QFile(fileDir) 
                if not self.localFile.open(QIODevice.ReadWrite):
                    del self.localFile
                    return 
                self.ftpClient.get(fileName,self.localFile)
    
    def slotPut(self):
        self.fileVewer.show()                     
        self.curStatus='PUT'
    def slotGet(self):                     
        self.fileVewer.show()
        self.curStatus='GET'

    def slotStateChanged(self,state):
    
        if(state == QFtp.LoggedIn):
        
            self.pushButtonPut.setEnabled(True)
            self.pushButtonGet.setEnabled(True)
        

        
import sys
app = QApplication(sys.argv)
c = FtpClient()
c.show()
app.exec_()