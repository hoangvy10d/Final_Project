# Form implementation generated from reading ui file 'D:\Users\LENOVO\baicuaThao\Final_Project\Login\LogIn.ui'
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
        self.label.setGeometry(QtCore.QRect(0, 0, 1171, 761))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\Users\\LENOVO\\baicuaThao\\Final_Project\\Login\\../image/log in.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButtonLogin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonLogin.setGeometry(QtCore.QRect(780, 550, 141, 51))
        self.pushButtonLogin.setText("")
        self.pushButtonLogin.setFlat(True)
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.lineEditLoginName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditLoginName.setGeometry(QtCore.QRect(790, 330, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditLoginName.setFont(font)
        self.lineEditLoginName.setStyleSheet("QLineEdit {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.lineEditLoginName.setObjectName("lineEditLoginName")
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditPassword.setGeometry(QtCore.QRect(790, 430, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setStyleSheet("QLineEdit {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.radioButtoUser = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButtoUser.setGeometry(QtCore.QRect(790, 490, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtoUser.setFont(font)
        self.radioButtoUser.setStyleSheet("color: rgb(147, 186, 70);")
        self.radioButtoUser.setObjectName("radioButtoUser")
        self.radioButtonManager = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButtonManager.setGeometry(QtCore.QRect(950, 490, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonManager.setFont(font)
        self.radioButtonManager.setStyleSheet("color: rgb(147, 186, 70);")
        self.radioButtonManager.setObjectName("radioButtonManager")
        self.pushButtonSignUp = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSignUp.setGeometry(QtCore.QRect(950, 550, 141, 51))
        self.pushButtonSignUp.setText("")
        self.pushButtonSignUp.setFlat(True)
        self.pushButtonSignUp.setObjectName("pushButtonSignUp")
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
        self.radioButtoUser.setText(_translate("MainWindow", "User"))
        self.radioButtonManager.setText(_translate("MainWindow", "Manager"))
