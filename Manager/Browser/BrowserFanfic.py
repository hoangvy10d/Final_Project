# Form implementation generated from reading ui file 'D:\Users\LENOVO\baicuaThao\Final_Project\Manager\Browser\BrowserFanfic.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1173, 809)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1171, 751))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\Users\\LENOVO\\baicuaThao\\Final_Project\\Manager\\Browser\\../../image/DUYỆT BÀI FANFIC.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 100, 621, 341))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(740, 30, 361, 431))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_Search = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEdit_Search.setMaximumSize(QtCore.QSize(16777215, 70))
        self.lineEdit_Search.setObjectName("lineEdit_Search")
        self.horizontalLayout_3.addWidget(self.lineEdit_Search)
        self.pushButton_Search = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_Search.setMinimumSize(QtCore.QSize(15, 35))
        self.pushButton_Search.setMaximumSize(QtCore.QSize(40, 70))
        self.pushButton_Search.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\Users\\LENOVO\\baicuaThao\\Final_Project\\Manager\\Browser\\../../image/icon/search.webp"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_Search.setIcon(icon)
        self.pushButton_Search.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.horizontalLayout_3.addWidget(self.pushButton_Search)
        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.listWidget = QtWidgets.QListWidget(parent=self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.lineEdit_Title = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_Title.setGeometry(QtCore.QRect(270, 520, 611, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_Title.setFont(font)
        self.lineEdit_Title.setStyleSheet("QLineEdit {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.lineEdit_Title.setText("")
        self.lineEdit_Title.setObjectName("lineEdit_Title")
        self.lineEdit_Character = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_Character.setGeometry(QtCore.QRect(270, 570, 611, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_Character.setFont(font)
        self.lineEdit_Character.setStyleSheet("QLineEdit {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.lineEdit_Character.setText("")
        self.lineEdit_Character.setObjectName("lineEdit_Character")
        self.lineEdit_Date = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_Date.setGeometry(QtCore.QRect(270, 620, 611, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_Date.setFont(font)
        self.lineEdit_Date.setStyleSheet("QLineEdit {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.lineEdit_Date.setText("")
        self.lineEdit_Date.setObjectName("lineEdit_Date")
        self.lineEdit_Author = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_Author.setGeometry(QtCore.QRect(270, 670, 611, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_Author.setFont(font)
        self.lineEdit_Author.setStyleSheet("QLineEdit {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.lineEdit_Author.setText("")
        self.lineEdit_Author.setObjectName("lineEdit_Author")
        self.pushButton_Approved = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Approved.setGeometry(QtCore.QRect(930, 507, 191, 51))
        self.pushButton_Approved.setText("")
        self.pushButton_Approved.setFlat(True)
        self.pushButton_Approved.setObjectName("pushButton_Approved")
        self.pushButton_Remove = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Remove.setGeometry(QtCore.QRect(930, 580, 191, 51))
        self.pushButton_Remove.setText("")
        self.pushButton_Remove.setFlat(True)
        self.pushButton_Remove.setObjectName("pushButton_Remove")
        self.pushButton_Back = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Back.setGeometry(QtCore.QRect(930, 660, 191, 51))
        self.pushButton_Back.setText("")
        self.pushButton_Back.setFlat(True)
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.pushButton_Exit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Exit.setGeometry(QtCore.QRect(1120, 0, 51, 51))
        self.pushButton_Exit.setText("")
        self.pushButton_Exit.setFlat(True)
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1173, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
