# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/ecc.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 70, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_generate = QtWidgets.QToolButton(self.centralwidget)
        self.btn_generate.setGeometry(QtCore.QRect(460, 90, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_generate.setFont(font)
        self.btn_generate.setObjectName("btn_generate")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(26, 180, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(26, 300, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btn_sign = QtWidgets.QToolButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(184, 448, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_sign.setFont(font)
        self.btn_sign.setObjectName("btn_sign")
        self.btn_verify = QtWidgets.QToolButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(490, 450, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_verify.setFont(font)
        self.btn_verify.setObjectName("btn_verify")
        self.txt_Info = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_Info.setGeometry(QtCore.QRect(170, 140, 491, 121))
        self.txt_Info.setObjectName("txt_Info")
        self.txt_sign = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(170, 290, 491, 141))
        self.txt_sign.setObjectName("txt_sign")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ECC CIPHER"))
        self.btn_generate.setText(_translate("MainWindow", "Generate Keys"))
        self.label_2.setText(_translate("MainWindow", "Information"))
        self.label_3.setText(_translate("MainWindow", "Signature"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
