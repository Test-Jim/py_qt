#coding:utf-8
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtNetwork import *
from fileViewer import FileDir

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
class FtpClient(QWidget):
    def __init__(self,parent=None):
        super(FtpClient,self).__init__(parent)
        self.setWindowTitle(u"FTP Client")
        self.fileVewer = FileDir()
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
        self.connect(self.treeWidget,SIGNAL("itemActivated(QTreeWidgetItem*,int)"),self.processItem)
        
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
        
        # hbLayout1 = QHBoxLayout()
        # self.returnButton = QPushButton(u"返回上一层")
        # self.enterButton = QPushButton(u"进入下一层")
        # self.mkdirButton = QPushButton(u"新建文件夹")
        # # self.delButton = QPushButton(u"删除")
        # hbLayout1.addWidget(self.returnButton)
        # hbLayout1.addWidget(self.enterButton)
        # hbLayout1.addWidget(self.mkdirButton)
        # hbLayout1.addWidget(self.delButton)
        # self.connect(self.returnButton,SIGNAL("clicked()"),self.slotReturn)
        # self.connect(self.enterButton,SIGNAL("clicked()"),self.slotEnter)
        # self.connect(self.mkdirButton,SIGNAL("clicked()"),self.slotMkdir)
        # self.connect(self.delButton, SIGNAL("clicked()"),self.slotDel)
        
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
        # self.returnButton.setEnabled(False)
        # self.enterButton.setEnabled(False)
        # self.mkdirButton.setEnabled(False)
        # self.delButton.setEnabled(False)
        
        self.curStatus=''
        self.delStatus=''
        self.delList = []
    # def slotDel(self):
    #     name = self.treeWidget.currentItem().text(1)
    #     if (self.isDirectory[name]): # //如果这个文件是个目录
    #         self.ftpClient.rmdir(name)
    #         QMessageBox.warning(self,u"tip",u"are you sure")
    #     else:
    #         self.ftpClient.remove(name)
    #
    #     self.treeWidget.clear()
    #     self.isDirectory.clear()
    #     self.ftpClient.list()
    def slotEnter(self):
        name = self.treeWidget.currentItem().text(1)
        if (self.isDirectory[name]): # //如果这个文件是个目录，则打开
            self.treeWidget.clear()
            self.isDirectory.clear()
            self.currentPath += '/'
            self.currentPath += name
            self.ftpClient.cd(name)
            self.ftpClient.list()
            self.returnButton.setEnabled(True)
        else:
            print "not a dir"
            pass
    def slotMkdir(self):
        dirName = QInputDialog.getText(None, u"创建文件夹",u"文件夹名称：",QLineEdit.Normal, u"新建文件夹")[0]
        print dirName
        #self.ftpClient.cd(self.currentPath)
        #self.ftpClient.mkdir(QString(QTextCodec.codecForName("utf-8").fromUnicode(dirName)))
        self.ftpClient.mkdir(QString(dirName))
        
        self.treeWidget.clear()
        self.isDirectory.clear()
        self.ftpClient.list()
        
    def slotReturn(self):
        #name = self.treeWidget.currentItem().text(1)
        self.treeWidget.clear()
        self.isDirectory.clear()
        #self.currentPath += '/'
        #self.currentPath += name
        print self.currentPath
        self.currentPath = self.currentPath.left(self.currentPath.lastIndexOf('/'))
        if (self.currentPath.isEmpty()):
            self.returnButton.setEnabled(False)
            self.ftpClient.cd("/")
        else:
            self.ftpClient.cd(self.currentPath)
            print self.currentPath
            
            
        self.ftpClient.list()
        print "return back"
                                                       
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

        self.isDirectory = {}


        # self.connect(self.ftpClient,SIGNAL("commandStarted(int)"),self.ftpCommandStarted)

        #self.connect(self.ftpClient, SIGNAL("done(bool)"),self.slotDone)

        self.connect(self.ftpClient,SIGNAL("commandFinished(int,bool)"),self.ftpCommandFinished)

        self.connect(self.ftpClient,SIGNAL("listInfo(QUrlInfo)"),self.addToList)

        self.connect(self.ftpClient,SIGNAL("dataTransferProgress(qint64,qint64)"),self.updateDataTransferProgress)
        
    def processItem(self,item,index):
        name = item.text(1)   
        #print name 
        if (self.isDirectory[name]): # //如果这个文件是个目录，则打开
            self.treeWidget.clear()
            self.isDirectory.clear()
            self.currentPath += '/'
            self.currentPath += name
            print self.currentPath
            self.ftpClient.cd(name)
            self.ftpClient.list()
            self.returnButton.setEnabled(True)
        else:
            print "not a dir"
            
        
    # def ftpCommandStarted(self):
    #     if(self.ftpClient.currentCommand() == QFtp.ConnectToHost):
    #
    #         print "connecting"
    #
    #
    #
    #     elif (self.ftpClient.currentCommand() == QFtp.Login):
    #
    #         print "logining"
    #
    #
    #
    #     elif (self.ftpClient.currentCommand() == QFtp.Get):
    #
    #         print "downloading"
    #
    #
    #
    #     elif (self.ftpClient.currentCommand() == QFtp.Close):
    #
    #         print "disconnecting"
    #
    #     elif (self.ftpClient.currentCommand() == QFtp.List):
    #
    #         print "listing"
            
    def ftpCommandFinished(self):
        #if erro:
            #QMessageBox.warning(self,u"erro",u"not null")
        if(self.ftpClient.currentCommand() == QFtp.ConnectToHost):

            print "connected"

        #elif(self.ftpClient.currentCommand()==QFtp.rmdir):
            #print "mmm"
            #QMessageBox.warning(self,u"error",u"not null")
    
        elif (self.ftpClient.currentCommand() == QFtp.Login):
    
            print "login"
            QMessageBox.information(self,u"succeed",u"登录成功!")
            self.pushButtonPut.setEnabled(True)
            self.pushButtonGet.setEnabled(True)
    
            self.ftpClient.list()   #发射listInfo()信号，显示文件列表
    
        elif (self.ftpClient.currentCommand() == QFtp.Get):
    
            print "download"
            #QMessageBox.information(self,u"succeed",u"Get file succeed!")
            
            self.pbar.setValue(0)
        elif (self.ftpClient.currentCommand()==QFtp.Put):
            print "put"
            self.pbar.setValue(0)
            
    
        
    
        elif (self.ftpClient.currentCommand() == QFtp.Close):
    
            print "disconnected"
        
        #if(error) ui->label->setText(tr(“连接服务器出现错误：%1″).arg(ftp->errorString()));
        #然后，在下载命令完成时，我们使下载按钮可用：
        #ui->downloadButton->setEnabled(true);

        #最后再添加一个if语句，处理list命令完成时的情况：

        elif (self.ftpClient.currentCommand() == QFtp.List):

            if (self.isDirectory == False):
                #如果目录为空,显示“empty”
                self.treeWidget.addTopLevelItem(QTreeWidgetItem(QStringList().tr("<empty>")))
                self.treeWidget.setEnabled(False)
                
                
            self.enterButton.setEnabled(True)
            self.mkdirButton.setEnabled(True)
            self.delButton.setEnabled(True)
            print "listed"

                #ui->label->setText(tr(“该目录为空”));     
    def addToList(self,urlInfo):
        if self.delStatus == '':
            print urlInfo
            name = str(urlInfo.name())
            print name.decode('gbk')
            print "addlist"
            item = QTreeWidgetItem(self.treeWidget)
            item.setFont(0, QFont("times",13,QFont.Bold))
            item.setText(1, urlInfo.name())
            item.setText(2, QString.number(urlInfo.size()))
            item.setText(3, urlInfo.owner())
            item.setText(4, urlInfo.group())
            item.setText(4, urlInfo.lastModified().toString('MMM dd yyyy'))
            pixmapdir = QPixmap("dir.png")
            pixmapfile = QPixmap("file.png")
            #pixmapdir = pixmapdir.scaled(30, 30)
            #pixmapfile = pixmapfile.scaled(30,30)
            
            if urlInfo.isDir():
                #item.setIcon(0,QIcon(pixmapdir))
                item.setText(0,u"文件夹")
            else:
                #item.setIcon(0,QIcon(pixmapfile))
                item.setText(0,u"文件")
            #存储该路径是否为目录的信息
            self.isDirectory[urlInfo.name()] = urlInfo.isDir()
            
            self.treeWidget.addTopLevelItem(item)
        
            if (not self.treeWidget.currentItem()):
                self.treeWidget.setCurrentItem(self.treeWidget.topLevelItem(0))
                self.treeWidget.setEnabled(True)
        elif self.delStatus == 'delete':
            print "namename"
            self.delList.append(urlInfo.name())
            print self.delList
            
            
    def updateDataTransferProgress(self,readByte,totalByte):
        if totalByte >= 4096:
            self.pbar.setMaximum(totalByte)
            self.pbar.setValue(readByte)
        else:
            pass
    def locate(self,dir,noydir):
        fileDir = QString(dir)
        print noydir
        if self.curStatus == 'PUT':
            if noydir == 'file':
                fileName,ok= QInputDialog.getText(self, u"Put File:",u"Please input file name:", QLineEdit.Normal, QString()) 
                if(ok and not fileName.isEmpty()):    
                    self.remoteFileName=QFile(fileDir)
                    if not self.remoteFileName.open(QIODevice.ReadWrite):
                        del self.remoteFileName
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
            fileName,ok= QInputDialog.getText(self, u"Put File:",u"Please input file name:", QLineEdit.Normal, QString()) 
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
        
        
    def slotGet_(self):
        fileName = self.treeWidget.currentItem().text(1)
        
        self.localFile= QFile("D:/") 
         
        if not self.localFile.open(QIODevice.ReadWrite):
            del self.localFile
            return 
            
        self.ftpClient.get(fileName,self.localFile)
            
        self.curStatus='GET'
    
    def slotGet__(self):
        fileName = self.treeWidget.currentItem().text(1)
        
        self.localFile= QFile("D:/") 
         
        if not self.localFile.open(QIODevice.ReadWrite):
            del self.localFile
            return 
            
        self.ftpClient.get(fileName,self.localFile)
            
        self.curStatus='GET'
    
    
    def slotStateChanged(self,state):
    
        if(state == QFtp.LoggedIn):
        
            self.pushButtonPut.setEnabled(True)
            self.pushButtonGet.setEnabled(True)
        
    
    
    # def slotDone(self,error):
    #
    #     if(self.curStatus == 'PUT'):
    #
    #         QMessageBox.information(self,u"succeed",u"Put file succeed!")
    #         self.curStatus=''
    #
    #     if(self.curStatus == 'GET'):
    #
    #         self.localFile.close()
    #         QMessageBox.information(self,u"succeed",u"Get file succeed!")
    #         self.curStatus=''
        
import sys
app = QApplication(sys.argv)
c = FtpClient()
c.show()
app.exec_()