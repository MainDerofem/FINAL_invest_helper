# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Final_version_passive_by_tendantion.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_inc_after_years(object):
    def setupUi(self, inc_after_years):
        inc_after_years.setObjectName("inc_after_years")
        inc_after_years.resize(830, 500)
        inc_after_years.setMinimumSize(QtCore.QSize(830, 500))
        inc_after_years.setMaximumSize(QtCore.QSize(830, 500))
        inc_after_years.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 219, 242, 255), stop:1 rgba(203, 255, 221, 255));}")
        self.centralwidget = QtWidgets.QWidget(inc_after_years)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 701, 131))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_back_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back_6.setGeometry(QtCore.QRect(730, 460, 75, 23))
        self.btn_back_6.setStyleSheet("background-color: rgb(143, 54, 36);\n"
"color: rgb(255, 255, 255);")
        self.btn_back_6.setObjectName("btn_back_6")
        self.btn_count_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_count_6.setGeometry(QtCore.QRect(550, 270, 250, 100))
        self.btn_count_6.setMinimumSize(QtCore.QSize(250, 100))
        self.btn_count_6.setMaximumSize(QtCore.QSize(250, 100))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_count_6.setFont(font)
        self.btn_count_6.setStyleSheet("color: rgb(0, 255, 128);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(133, 170, 255);")
        self.btn_count_6.setObjectName("btn_count_6")
        self.Answer_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.Answer_6.setGeometry(QtCore.QRect(20, 390, 781, 51))
        self.Answer_6.setObjectName("Answer_6")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 150, 518, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(31, 31, 31);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.cap_las_year_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.cap_las_year_6.setObjectName("cap_las_year_6")
        self.horizontalLayout.addWidget(self.cap_las_year_6)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(31, 31, 31);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.cap_penultimate_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.cap_penultimate_6.setObjectName("cap_penultimate_6")
        self.horizontalLayout_2.addWidget(self.cap_penultimate_6)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        inc_after_years.setCentralWidget(self.centralwidget)

        self.retranslateUi(inc_after_years)
        QtCore.QMetaObject.connectSlotsByName(inc_after_years)

    def retranslateUi(self, inc_after_years):
        _translate = QtCore.QCoreApplication.translate
        inc_after_years.setWindowTitle(_translate("inc_after_years", "?????????????? ???????????????????? ????????????"))
        self.label.setText(_translate("inc_after_years", "<html><head/><body><p align=\"center\">???????????????? ???????????????????? ?????????? ???????????????????? ???????????? (?? ??????????),</p><p align=\"center\">?????????? ?????????????????? ???????? ???????????????????? ??????.</p></body></html>"))
        self.btn_back_6.setText(_translate("inc_after_years", "??????????"))
        self.btn_count_6.setText(_translate("inc_after_years", "????????????????????!"))
        self.label_6.setText(_translate("inc_after_years", "?????????? ???????????????? ???? ?????????? ???????????????????? ????????:       "))
        self.label_10.setText(_translate("inc_after_years", "??????."))
        self.label_7.setText(_translate("inc_after_years", "?????????? ???????????????? ???? ?????????? ???????????????????????????? ????????:"))
        self.label_11.setText(_translate("inc_after_years", "??????."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inc_after_years = QtWidgets.QMainWindow()
    inc_years = Ui_inc_after_years()
    inc_years.setupUi(inc_after_years)
    inc_after_years.show()
    sys.exit(app.exec_())
