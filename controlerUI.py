# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controler.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btStart = QtWidgets.QPushButton(self.centralwidget)
        self.btStart.setGeometry(QtCore.QRect(575, 420, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btStart.setFont(font)
        self.btStart.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.btStart.setObjectName("btStart")
        self.btnStop = QtWidgets.QPushButton(self.centralwidget)
        self.btnStop.setEnabled(False)
        self.btnStop.setGeometry(QtCore.QRect(460, 420, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnStop.setFont(font)
        self.btnStop.setStyleSheet("background-color: rgb(85, 0, 0);")
        self.btnStop.setObjectName("btnStop")
        self.btnEnd = QtWidgets.QPushButton(self.centralwidget)
        self.btnEnd.setGeometry(QtCore.QRect(20, 420, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnEnd.setFont(font)
        self.btnEnd.setStyleSheet("background-color: rgb(37, 0, 111);")
        self.btnEnd.setObjectName("btnEnd")
        self.gbStation1 = QtWidgets.QGroupBox(self.centralwidget)
        self.gbStation1.setGeometry(QtCore.QRect(300, 10, 151, 120))
        self.gbStation1.setStyleSheet("QGroupBox {\n"
"    border: 1px solid white;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.gbStation1.setCheckable(True)
        self.gbStation1.setObjectName("gbStation1")
        self.lblSt1Smpl1 = QtWidgets.QLabel(self.gbStation1)
        self.lblSt1Smpl1.setGeometry(QtCore.QRect(10, 20, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblSt1Smpl1.setFont(font)
        self.lblSt1Smpl1.setObjectName("lblSt1Smpl1")
        self.lblSt1Smpl1State = QtWidgets.QLabel(self.gbStation1)
        self.lblSt1Smpl1State.setGeometry(QtCore.QRect(110, 20, 20, 20))
        self.lblSt1Smpl1State.setStyleSheet("border: 1px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);")
        self.lblSt1Smpl1State.setText("")
        self.lblSt1Smpl1State.setObjectName("lblSt1Smpl1State")
        self.lblSt1Smpl2 = QtWidgets.QLabel(self.gbStation1)
        self.lblSt1Smpl2.setGeometry(QtCore.QRect(10, 55, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblSt1Smpl2.setFont(font)
        self.lblSt1Smpl2.setObjectName("lblSt1Smpl2")
        self.lblSt1Smpl2State = QtWidgets.QLabel(self.gbStation1)
        self.lblSt1Smpl2State.setGeometry(QtCore.QRect(110, 55, 20, 20))
        self.lblSt1Smpl2State.setStyleSheet("border: 1px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);")
        self.lblSt1Smpl2State.setText("")
        self.lblSt1Smpl2State.setObjectName("lblSt1Smpl2State")
        self.lblSt1Smpl3 = QtWidgets.QLabel(self.gbStation1)
        self.lblSt1Smpl3.setGeometry(QtCore.QRect(10, 90, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblSt1Smpl3.setFont(font)
        self.lblSt1Smpl3.setObjectName("lblSt1Smpl3")
        self.lblSt1Smpl3State = QtWidgets.QLabel(self.gbStation1)
        self.lblSt1Smpl3State.setGeometry(QtCore.QRect(110, 90, 20, 20))
        self.lblSt1Smpl3State.setStyleSheet("border: 1px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);")
        self.lblSt1Smpl3State.setText("")
        self.lblSt1Smpl3State.setObjectName("lblSt1Smpl3State")
        self.logView = QtWidgets.QTextEdit(self.centralwidget)
        self.logView.setGeometry(QtCore.QRect(10, 10, 270, 301))
        self.logView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.logView.setReadOnly(True)
        self.logView.setObjectName("logView")
        self.gbStation2 = QtWidgets.QGroupBox(self.centralwidget)
        self.gbStation2.setGeometry(QtCore.QRect(300, 140, 151, 120))
        self.gbStation2.setStyleSheet("QGroupBox {\n"
"    border: 1px solid white;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.gbStation2.setCheckable(True)
        self.gbStation2.setObjectName("gbStation2")
        self.lblSt2Smpl1 = QtWidgets.QLabel(self.gbStation2)
        self.lblSt2Smpl1.setGeometry(QtCore.QRect(10, 20, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblSt2Smpl1.setFont(font)
        self.lblSt2Smpl1.setObjectName("lblSt2Smpl1")
        self.lblSt2Smpl1State = QtWidgets.QLabel(self.gbStation2)
        self.lblSt2Smpl1State.setGeometry(QtCore.QRect(110, 20, 20, 20))
        self.lblSt2Smpl1State.setStyleSheet("border: 1px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);")
        self.lblSt2Smpl1State.setText("")
        self.lblSt2Smpl1State.setObjectName("lblSt2Smpl1State")
        self.lblSt2Smpl2 = QtWidgets.QLabel(self.gbStation2)
        self.lblSt2Smpl2.setGeometry(QtCore.QRect(10, 55, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblSt2Smpl2.setFont(font)
        self.lblSt2Smpl2.setObjectName("lblSt2Smpl2")
        self.lblSt2Smpl2State = QtWidgets.QLabel(self.gbStation2)
        self.lblSt2Smpl2State.setGeometry(QtCore.QRect(110, 55, 20, 20))
        self.lblSt2Smpl2State.setStyleSheet("border: 1px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);")
        self.lblSt2Smpl2State.setText("")
        self.lblSt2Smpl2State.setObjectName("lblSt2Smpl2State")
        self.lblSt2Smpl3 = QtWidgets.QLabel(self.gbStation2)
        self.lblSt2Smpl3.setGeometry(QtCore.QRect(10, 90, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblSt2Smpl3.setFont(font)
        self.lblSt2Smpl3.setObjectName("lblSt2Smpl3")
        self.lblSt2Smpl3State = QtWidgets.QLabel(self.gbStation2)
        self.lblSt2Smpl3State.setGeometry(QtCore.QRect(110, 90, 20, 20))
        self.lblSt2Smpl3State.setStyleSheet("border: 1px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);")
        self.lblSt2Smpl3State.setText("")
        self.lblSt2Smpl3State.setObjectName("lblSt2Smpl3State")
        self.gbStation3 = QtWidgets.QGroupBox(self.centralwidget)
        self.gbStation3.setGeometry(QtCore.QRect(300, 270, 151, 120))
        self.gbStation3.setStyleSheet("QGroupBox {\n"
"    border: 1px solid white;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.gbStation3.setCheckable(True)
        self.gbStation3.setObjectName("gbStation3")
        self.lblSt3Smpl1 = QtWidgets.QLabel(self.gbStation3)
        self.lblSt3Smpl1.setGeometry(QtCore.QRect(10, 20, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblSt3Smpl1.setFont(font)
        self.lblSt3Smpl1.setObjectName("lblSt3Smpl1")
        self.lblSt3Smpl1State = QtWidgets.QLabel(self.gbStation3)
        self.lblSt3Smpl1State.setGeometry(QtCore.QRect(110, 20, 20, 20))
        self.lblSt3Smpl1State.setStyleSheet("border: 1px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);")
        self.lblSt3Smpl1State.setText("")
        self.lblSt3Smpl1State.setObjectName("lblSt3Smpl1State")
        self.lblSt3Smpl2 = QtWidgets.QLabel(self.gbStation3)
        self.lblSt3Smpl2.setGeometry(QtCore.QRect(10, 55, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblSt3Smpl2.setFont(font)
        self.lblSt3Smpl2.setObjectName("lblSt3Smpl2")
        self.lblSt3Smpl2State = QtWidgets.QLabel(self.gbStation3)
        self.lblSt3Smpl2State.setGeometry(QtCore.QRect(110, 55, 20, 20))
        self.lblSt3Smpl2State.setStyleSheet("border: 1px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);")
        self.lblSt3Smpl2State.setText("")
        self.lblSt3Smpl2State.setObjectName("lblSt3Smpl2State")
        self.lblSt3Smpl3 = QtWidgets.QLabel(self.gbStation3)
        self.lblSt3Smpl3.setGeometry(QtCore.QRect(10, 90, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblSt3Smpl3.setFont(font)
        self.lblSt3Smpl3.setObjectName("lblSt3Smpl3")
        self.lblSt3Smpl3State = QtWidgets.QLabel(self.gbStation3)
        self.lblSt3Smpl3State.setGeometry(QtCore.QRect(110, 90, 20, 20))
        self.lblSt3Smpl3State.setStyleSheet("border: 1px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);")
        self.lblSt3Smpl3State.setText("")
        self.lblSt3Smpl3State.setObjectName("lblSt3Smpl3State")
        self.tBtnFileSelect = QtWidgets.QPushButton(self.centralwidget)
        self.tBtnFileSelect.setGeometry(QtCore.QRect(250, 360, 29, 29))
        self.tBtnFileSelect.setObjectName("tBtnFileSelect")
        self.lblReportFileName = QtWidgets.QLabel(self.centralwidget)
        self.lblReportFileName.setGeometry(QtCore.QRect(10, 340, 91, 20))
        self.lblReportFileName.setObjectName("lblReportFileName")
        self.lEditFileName = QtWidgets.QLineEdit(self.centralwidget)
        self.lEditFileName.setGeometry(QtCore.QRect(10, 360, 231, 29))
        self.lEditFileName.setObjectName("lEditFileName")
        self.gbParams = QtWidgets.QGroupBox(self.centralwidget)
        self.gbParams.setGeometry(QtCore.QRect(460, 10, 231, 171))
        self.gbParams.setStyleSheet("QGroupBox {\n"
"    border: 1px solid white;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.gbParams.setCheckable(False)
        self.gbParams.setObjectName("gbParams")
        self.sBoxCycleCounter = QtWidgets.QSpinBox(self.gbParams)
        self.sBoxCycleCounter.setGeometry(QtCore.QRect(135, 133, 80, 22))
        self.sBoxCycleCounter.setAlignment(QtCore.Qt.AlignCenter)
        self.sBoxCycleCounter.setMaximum(9999)
        self.sBoxCycleCounter.setProperty("value", 10)
        self.sBoxCycleCounter.setObjectName("sBoxCycleCounter")
        self.sBoxInAirTime = QtWidgets.QSpinBox(self.gbParams)
        self.sBoxInAirTime.setGeometry(QtCore.QRect(135, 106, 80, 22))
        self.sBoxInAirTime.setAlignment(QtCore.Qt.AlignCenter)
        self.sBoxInAirTime.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sBoxInAirTime.setSpecialValueText("")
        self.sBoxInAirTime.setMaximum(9999)
        self.sBoxInAirTime.setProperty("value", 10)
        self.sBoxInAirTime.setObjectName("sBoxInAirTime")
        self.sBoxFillTime = QtWidgets.QSpinBox(self.gbParams)
        self.sBoxFillTime.setGeometry(QtCore.QRect(135, 22, 80, 22))
        self.sBoxFillTime.setAlignment(QtCore.Qt.AlignCenter)
        self.sBoxFillTime.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sBoxFillTime.setMaximum(9999)
        self.sBoxFillTime.setProperty("value", 60)
        self.sBoxFillTime.setObjectName("sBoxFillTime")
        self.sBoxDischargeTime = QtWidgets.QSpinBox(self.gbParams)
        self.sBoxDischargeTime.setGeometry(QtCore.QRect(135, 79, 80, 22))
        self.sBoxDischargeTime.setAlignment(QtCore.Qt.AlignCenter)
        self.sBoxDischargeTime.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sBoxDischargeTime.setSpecialValueText("")
        self.sBoxDischargeTime.setMaximum(9999)
        self.sBoxDischargeTime.setProperty("value", 60)
        self.sBoxDischargeTime.setObjectName("sBoxDischargeTime")
        self.sBoxInFluidTime = QtWidgets.QSpinBox(self.gbParams)
        self.sBoxInFluidTime.setGeometry(QtCore.QRect(135, 51, 80, 22))
        self.sBoxInFluidTime.setAlignment(QtCore.Qt.AlignCenter)
        self.sBoxInFluidTime.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sBoxInFluidTime.setSpecialValueText("")
        self.sBoxInFluidTime.setMaximum(9999)
        self.sBoxInFluidTime.setProperty("value", 10)
        self.sBoxInFluidTime.setObjectName("sBoxInFluidTime")
        self.pBtnFill = QtWidgets.QPushButton(self.gbParams)
        self.pBtnFill.setGeometry(QtCore.QRect(10, 22, 120, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pBtnFill.setFont(font)
        self.pBtnFill.setFlat(True)
        self.pBtnFill.setObjectName("pBtnFill")
        self.pBtnInFluid = QtWidgets.QPushButton(self.gbParams)
        self.pBtnInFluid.setGeometry(QtCore.QRect(10, 51, 120, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pBtnInFluid.setFont(font)
        self.pBtnInFluid.setFlat(True)
        self.pBtnInFluid.setObjectName("pBtnInFluid")
        self.pBtnDischarge = QtWidgets.QPushButton(self.gbParams)
        self.pBtnDischarge.setGeometry(QtCore.QRect(10, 79, 120, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pBtnDischarge.setFont(font)
        self.pBtnDischarge.setFlat(True)
        self.pBtnDischarge.setObjectName("pBtnDischarge")
        self.pBtnInAir = QtWidgets.QPushButton(self.gbParams)
        self.pBtnInAir.setGeometry(QtCore.QRect(10, 106, 120, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pBtnInAir.setFont(font)
        self.pBtnInAir.setFlat(True)
        self.pBtnInAir.setObjectName("pBtnInAir")
        self.pBtnCycleCounter = QtWidgets.QPushButton(self.gbParams)
        self.pBtnCycleCounter.setGeometry(QtCore.QRect(10, 133, 120, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pBtnCycleCounter.setFont(font)
        self.pBtnCycleCounter.setFlat(True)
        self.pBtnCycleCounter.setObjectName("pBtnCycleCounter")
        self.pBarStateProgress = QtWidgets.QProgressBar(self.centralwidget)
        self.pBarStateProgress.setGeometry(QtCore.QRect(470, 270, 211, 23))
        self.pBarStateProgress.setProperty("value", 0)
        self.pBarStateProgress.setObjectName("pBarStateProgress")
        self.lblActualCycle = QtWidgets.QLabel(self.centralwidget)
        self.lblActualCycle.setGeometry(QtCore.QRect(470, 210, 220, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblActualCycle.setFont(font)
        self.lblActualCycle.setObjectName("lblActualCycle")
        self.lblActualState = QtWidgets.QLabel(self.centralwidget)
        self.lblActualState.setGeometry(QtCore.QRect(470, 240, 220, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblActualState.setFont(font)
        self.lblActualState.setObjectName("lblActualState")
        self.pBtnStation1 = QtWidgets.QPushButton(self.centralwidget)
        self.pBtnStation1.setGeometry(QtCore.QRect(295, 70, 1, 1))
        font = QtGui.QFont()
        font.setPointSize(2)
        font.setBold(True)
        font.setWeight(75)
        self.pBtnStation1.setFont(font)
        self.pBtnStation1.setText("")
        self.pBtnStation1.setFlat(True)
        self.pBtnStation1.setObjectName("pBtnStation1")
        self.pBtnStation2 = QtWidgets.QPushButton(self.centralwidget)
        self.pBtnStation2.setGeometry(QtCore.QRect(295, 200, 1, 1))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pBtnStation2.setFont(font)
        self.pBtnStation2.setText("")
        self.pBtnStation2.setFlat(True)
        self.pBtnStation2.setObjectName("pBtnStation2")
        self.pBtnStation3 = QtWidgets.QPushButton(self.centralwidget)
        self.pBtnStation3.setGeometry(QtCore.QRect(295, 330, 1, 1))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pBtnStation3.setFont(font)
        self.pBtnStation3.setText("")
        self.pBtnStation3.setFlat(True)
        self.pBtnStation3.setObjectName("pBtnStation3")
        self.pBtnClearLog = QtWidgets.QPushButton(self.centralwidget)
        self.pBtnClearLog.setGeometry(QtCore.QRect(148, 320, 131, 29))
        self.pBtnClearLog.setObjectName("pBtnClearLog")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lab Control"))
        self.btStart.setText(_translate("MainWindow", "START - F5"))
        self.btStart.setShortcut(_translate("MainWindow", "F5"))
        self.btnStop.setText(_translate("MainWindow", "STOP - F6"))
        self.btnStop.setShortcut(_translate("MainWindow", "F6"))
        self.btnEnd.setText(_translate("MainWindow", "KONIEC - F12"))
        self.btnEnd.setShortcut(_translate("MainWindow", "F12"))
        self.gbStation1.setTitle(_translate("MainWindow", "Stanowisko 1"))
        self.lblSt1Smpl1.setText(_translate("MainWindow", "PRÓBKA 1"))
        self.lblSt1Smpl2.setText(_translate("MainWindow", "PRÓBKA 2"))
        self.lblSt1Smpl3.setText(_translate("MainWindow", "PRÓBKA 3"))
        self.logView.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.gbStation2.setTitle(_translate("MainWindow", "Stanowisko 2"))
        self.lblSt2Smpl1.setText(_translate("MainWindow", "PRÓBKA 1"))
        self.lblSt2Smpl2.setText(_translate("MainWindow", "PRÓBKA 2"))
        self.lblSt2Smpl3.setText(_translate("MainWindow", "PRÓBKA 3"))
        self.gbStation3.setTitle(_translate("MainWindow", "Stanowisko 3"))
        self.lblSt3Smpl1.setText(_translate("MainWindow", "PRÓBKA 1"))
        self.lblSt3Smpl2.setText(_translate("MainWindow", "PRÓBKA 2"))
        self.lblSt3Smpl3.setText(_translate("MainWindow", "PRÓBKA 3"))
        self.tBtnFileSelect.setText(_translate("MainWindow", "..."))
        self.tBtnFileSelect.setShortcut(_translate("MainWindow", "F4"))
        self.lblReportFileName.setText(_translate("MainWindow", "Plik raportu:"))
        self.gbParams.setTitle(_translate("MainWindow", "Parametry testu"))
        self.sBoxInAirTime.setSuffix(_translate("MainWindow", " m"))
        self.sBoxFillTime.setSuffix(_translate("MainWindow", " s"))
        self.sBoxDischargeTime.setSuffix(_translate("MainWindow", " s"))
        self.sBoxInFluidTime.setSuffix(_translate("MainWindow", " m"))
        self.pBtnFill.setText(_translate("MainWindow", "NALEWANIE"))
        self.pBtnFill.setShortcut(_translate("MainWindow", "Alt+N"))
        self.pBtnInFluid.setText(_translate("MainWindow", "W CIECZY"))
        self.pBtnInFluid.setShortcut(_translate("MainWindow", "Alt+C"))
        self.pBtnDischarge.setText(_translate("MainWindow", "WYLEWANIE"))
        self.pBtnDischarge.setShortcut(_translate("MainWindow", "Alt+W"))
        self.pBtnInAir.setText(_translate("MainWindow", "W POWIETRZU"))
        self.pBtnInAir.setShortcut(_translate("MainWindow", "Alt+P"))
        self.pBtnCycleCounter.setText(_translate("MainWindow", "LICZBA CYKLI"))
        self.pBtnCycleCounter.setShortcut(_translate("MainWindow", "Alt+L"))
        self.lblActualCycle.setText(_translate("MainWindow", "Aktualny cykl:"))
        self.lblActualState.setText(_translate("MainWindow", "Stan próbki:"))
        self.pBtnStation1.setShortcut(_translate("MainWindow", "F1"))
        self.pBtnStation2.setShortcut(_translate("MainWindow", "F2"))
        self.pBtnStation3.setShortcut(_translate("MainWindow", "F3"))
        self.pBtnClearLog.setText(_translate("MainWindow", "WYCZYŚC LOG"))
        self.pBtnClearLog.setShortcut(_translate("MainWindow", "F4"))

