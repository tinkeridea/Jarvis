# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jarvisUi(object):
    def setupUi(self, jarvisUi):
        jarvisUi.setObjectName("jarvisUi")
        jarvisUi.resize(1423, 811)
        self.centralwidget = QtWidgets.QWidget(jarvisUi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 0, 2141, 861))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Pictures/Saved Pictures/7LP8.gif"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 740, 111, 41))
        self.pushButton.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 248, 43);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(730, 740, 111, 41))
        self.pushButton_2.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(214, 17, 53);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(960, 480, 461, 331))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Pictures/Saved Pictures/iron-man-jarvis-gif-5.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, -10, 581, 171))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Pictures/Saved Pictures/AgileFixedBichonfrise-size_restricted.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(580, -40, 261, 161))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../Pictures/Saved Pictures/J.A.R.V.I.S-Live-Wallpaper-GIF.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(840, -80, 581, 241))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../Pictures/Saved Pictures/8ee7d93c9b015c00938a4091c3ef443e951d1518_hq.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(910, 160, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:20px")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1150, 160, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:20px")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 190, 221, 241))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../../Pictures/Saved Pictures/wm59k.gif"))
        self.label_8.setScaledContents(False)
        self.label_8.setObjectName("label_8")
        jarvisUi.setCentralWidget(self.centralwidget)

        self.retranslateUi(jarvisUi)
        QtCore.QMetaObject.connectSlotsByName(jarvisUi)

    def retranslateUi(self, jarvisUi):
        _translate = QtCore.QCoreApplication.translate
        jarvisUi.setWindowTitle(_translate("jarvisUi", "jarvisUi"))
        self.pushButton.setText(_translate("jarvisUi", "Run"))
        self.pushButton_2.setText(_translate("jarvisUi", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jarvisUi = QtWidgets.QMainWindow()
    ui = Ui_jarvisUi()
    ui.setupUi(jarvisUi)
    jarvisUi.show()
    sys.exit(app.exec_())
