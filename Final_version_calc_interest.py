# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Final_version_calc_interest.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calc_Interest_Main(object):
    def setupUi(self, Calc_Interest_Main):
        Calc_Interest_Main.setObjectName("Calc_Interest_Main")
        Calc_Interest_Main.resize(830, 500)
        Calc_Interest_Main.setMinimumSize(QtCore.QSize(830, 500))
        Calc_Interest_Main.setMaximumSize(QtCore.QSize(830, 500))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(14)
        Calc_Interest_Main.setFont(font)
        Calc_Interest_Main.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.222, y1:0.0852273, x2:0.545, y2:0.857955, stop:0 rgba(222, 198, 255, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.centralwidget = QtWidgets.QWidget(Calc_Interest_Main)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 801, 61))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 247, 254);\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.btn_back_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back_2.setGeometry(QtCore.QRect(710, 460, 75, 23))
        self.btn_back_2.setStyleSheet("background-color: rgb(117, 19, 255);\n"
"color: rgb(210, 228, 255);")
        self.btn_back_2.setObjectName("btn_back_2")
        self.btn_count_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_count_2.setGeometry(QtCore.QRect(540, 280, 250, 100))
        self.btn_count_2.setMinimumSize(QtCore.QSize(250, 100))
        self.btn_count_2.setMaximumSize(QtCore.QSize(250, 100))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_count_2.setFont(font)
        self.btn_count_2.setStyleSheet("color: rgb(0, 255, 128);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(133, 170, 255);")
        self.btn_count_2.setObjectName("btn_count_2")
        self.Answer_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Answer_2.setGeometry(QtCore.QRect(10, 400, 781, 51))
        self.Answer_2.setObjectName("Answer_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 100, 481, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(31, 31, 31);")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.Summa_vkld_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Summa_vkld_2.setObjectName("Summa_vkld_2")
        self.horizontalLayout_5.addWidget(self.Summa_vkld_2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(31, 31, 31);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.Srok_razm_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Srok_razm_2.setObjectName("Srok_razm_2")
        self.horizontalLayout_6.addWidget(self.Srok_razm_2)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(31, 31, 31);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.Stavka_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Stavka_2.setObjectName("Stavka_2")
        self.horizontalLayout_7.addWidget(self.Stavka_2)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(31, 31, 31);\n"
"")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.Period_vilp_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Period_vilp_2.setObjectName("Period_vilp_2")
        self.horizontalLayout.addWidget(self.Period_vilp_2)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.verticalLayout.addLayout(self.horizontalLayout)
        Calc_Interest_Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calc_Interest_Main)
        QtCore.QMetaObject.connectSlotsByName(Calc_Interest_Main)

    def retranslateUi(self, Calc_Interest_Main):
        _translate = QtCore.QCoreApplication.translate
        Calc_Interest_Main.setWindowTitle(_translate("Calc_Interest_Main", "?????????????????????? ?????????????? ??????????????????"))
        self.label.setText(_translate("Calc_Interest_Main", "<html><head/><body><p><span style=\" font-size:14pt;\">?????? ?????????????? ?????????????????????? ?????????????? ??????????????????. ?????????????? ???? ???????????? ?????? ?????? ????????????????????????)</span></p></body></html>"))
        self.btn_back_2.setText(_translate("Calc_Interest_Main", "??????????"))
        self.btn_count_2.setText(_translate("Calc_Interest_Main", "????????????????????!"))
        self.label_9.setText(_translate("Calc_Interest_Main", "?????????? ????????????:                               "))
        self.label_5.setText(_translate("Calc_Interest_Main", "??????. "))
        self.label_6.setText(_translate("Calc_Interest_Main", "???????? ????????????????????:                         "))
        self.label_10.setText(_translate("Calc_Interest_Main", "??????  "))
        self.label_7.setText(_translate("Calc_Interest_Main", "???????????????????? ????????????:                      "))
        self.label_11.setText(_translate("Calc_Interest_Main", "%    "))
        self.label_8.setText(_translate("Calc_Interest_Main", "?????????????????????????? ????????????:                "))
        self.label_12.setText(_translate("Calc_Interest_Main", "?? ??????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calc_Interest_Main = QtWidgets.QMainWindow()
    calc_int = Ui_Calc_Interest_Main()
    calc_int.setupUi(Calc_Interest_Main)
    Calc_Interest_Main.show()
    sys.exit(app.exec_())
