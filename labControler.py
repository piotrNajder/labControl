import sys
from enum import Enum
from controlerUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QTimer, QObject
from test_station_controler.stationControler import stationControler as stCtrl
from test_station_controler.stationControler import PumpState as pS
from Adafruit_BBIO import GPIO
import datetime
import time

class Main(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.initControlsCallbacks()

        self.st1 = stCtrl(self, 1)
        self.st2 = stCtrl(self, 2)
        self.st3 = stCtrl(self, 3)

        self.setStationsGuiControls()
        self.setStationsWriteMethods()
        self.setStationsIos()
        self.setStationsTimersCallbacks()

    def setStationsGuiControls(self):
        self.st1.StateLabel = self.lblActCyc_St1
        self.st2.StateLabel = self.lblActCyc_St2
        self.st3.StateLabel = self.lblActCyc_St3
        
        self.st1.PhaseLabel = self.lblActPhase_St1
        self.st2.PhaseLabel = self.lblActPhase_St2
        self.st3.PhaseLabel = self.lblActPhase_St3

        self.st1.ProgressBar = self.pBarPhasePrgs_St1
        self.st2.ProgressBar = self.pBarPhasePrgs_St2
        self.st3.ProgressBar = self.pBarPhasePrgs_St3

        self.st1.In1StatusLabel = self.lblSt1Smpl1State
        self.st1.In2StatusLabel = self.lblSt1Smpl2State
        self.st1.In3StatusLabel = self.lblSt1Smpl3State

        self.st2.In1StatusLabel = self.lblSt2Smpl1State
        self.st2.In2StatusLabel = self.lblSt2Smpl2State
        self.st2.In3StatusLabel = self.lblSt2Smpl3State

        self.st3.In1StatusLabel = self.lblSt3Smpl1State
        self.st3.In2StatusLabel = self.lblSt3Smpl2State
        self.st3.In3StatusLabel = self.lblSt3Smpl3State

    def setStationsWriteMethods(self):
        self.st1._writeLog = self.writeLog
        self.st2._writeLog = self.writeLog
        self.st3._writeLog = self.writeLog

        self.st1._writeReport = self.writeReport
        self.st2._writeReport = self.writeReport
        self.st3._writeReport = self.writeReport

        self.st1.endOfTestCallback = self.stationEndOfTestCallback
        self.st2.endOfTestCallback = self.stationEndOfTestCallback
        self.st3.endOfTestCallback = self.stationEndOfTestCallback

    def setStationsIos(self):
        self.st1._inputs.sample1 = "P8_9"
        self.st1._inputs.sample2 = "P8_11"
        self.st1._inputs.sample3 = "P8_15"
        self.st1._outputs.runOut = "P9_23"
        self.st1._outputs.dirOut = "P9_41"

        self.st1.initIos()

        self.st2._inputs.sample1 = "P8_14"
        self.st2._inputs.sample2 = "P8_16"
        self.st2._inputs.sample3 = "P8_7"
        self.st2._outputs.runOut = "P9_12"
        self.st2._outputs.dirOut = "P9_15"

        self.st2.initIos()

        self.st3._inputs.sample1 = "P8_8"
        self.st3._inputs.sample2 = "P8_10"
        self.st3._inputs.sample3 = "P8_12"
        self.st3._outputs.runOut = "P9_30"
        self.st3._outputs.dirOut = "P9_27"

        self.st3.initIos()

    def initControlsCallbacks(self):
        self.btPathSelect.clicked.connect(lambda: self.btPathSelect_Clicked())

        self.btStart_St1.clicked.connect(lambda: self.btStart_Clicked())
        self.btStart_St2.clicked.connect(lambda: self.btStart_Clicked())
        self.btStart_St3.clicked.connect(lambda: self.btStart_Clicked())

        self.btStop_St1.clicked.connect(lambda: self.btStop_Clicked())
        self.btStop_St2.clicked.connect(lambda: self.btStop_Clicked())
        self.btStop_St3.clicked.connect(lambda: self.btStop_Clicked())

        self.btFill_St1.pressed.connect(lambda:self.btFill_Pressed())
        self.btFill_St2.pressed.connect(lambda:self.btFill_Pressed())
        self.btFill_St3.pressed.connect(lambda:self.btFill_Pressed())

        self.btFill_St1.released.connect(lambda:self.btFill_Released())
        self.btFill_St2.released.connect(lambda:self.btFill_Released())
        self.btFill_St3.released.connect(lambda:self.btFill_Released())

        self.btDischarge_St1.pressed.connect(lambda:self.btDischarge_Pressed())
        self.btDischarge_St2.pressed.connect(lambda:self.btDischarge_Pressed())
        self.btDischarge_St3.pressed.connect(lambda:self.btDischarge_Pressed())

        self.btDischarge_St1.released.connect(lambda:self.btDischarge_Released())
        self.btDischarge_St2.released.connect(lambda:self.btDischarge_Released())
        self.btDischarge_St3.released.connect(lambda:self.btDischarge_Released())
        
        self.pBtnClearLog.clicked.connect(lambda: self.pBtnClearLogClicked())

    def setStationsTimersCallbacks(self):
        self.st1._ioTimer.timeout.connect(self.st1_ioTimerCallback)
        self.st1._ioTimer.start(20)
        time.sleep(0.005)

        self.st2._ioTimer.timeout.connect(self.st2_ioTimerCallback)
        self.st2._ioTimer.start(20)
        time.sleep(0.005)

        self.st3._ioTimer.timeout.connect(self.st3_ioTimerCallback)
        self.st3._ioTimer.start(20)

        self.st1._cycleTimer.timeout.connect(self.st1_cycleTimerCallback)
        time.sleep(0.2)
        self.st2._cycleTimer.timeout.connect(self.st2_cycleTimerCallback)
        time.sleep(0.2)
        self.st3._cycleTimer.timeout.connect(self.st3_cycleTimerCallback)
 
    def writeLog(self, lvl, msg):
        cursor = self.logView.textCursor()

        alertHtml = "<font color=\"DarkRed \">"
        notifyHtml = "<font color=\"DarkGreen \">"
        infoHtml = "<font color=\"Black\">"
        endHtml = "</font><br>"
        line = ""
        timeStr = datetime.datetime.now().strftime("[%y.%m.%d - %H:%M:%S] ")
        if lvl == "Alert":
            line = alertHtml + timeStr + msg
        elif lvl == "Notify":
            line = notifyHtml + timeStr + msg
        else:
            line = infoHtml + timeStr + msg

        line += endHtml
        self.logView.insertHtml(line)
        cursor.movePosition(11) # 11 = QTextCursor::END
        self.logView.setTextCursor(cursor)

    def writeReport(self, station, msg):
        fName = ""
        if station == 1:
            fName = self.st1ReportName
        elif station == 2:
            fName = self.st2ReportName
        elif station == 3:
            fName = self.st3ReportName

        with open(fName, "a") as repF:
            l = datetime.datetime.now().strftime("[%y.%m.%d - %H:%M:%S] ") + msg + "\n"
            repF.write(l)

    def stationEndOfTestCallback(self, stationId):
        if stationId == "1":
            self.btStart_St1.setDisabled(False)
            self.btStop_St1.setDisabled(True)
            self.lblSt1RunState.setStyleSheet(self.StatuslblStyleSheet("RED"))
        elif stationId == "2":
            self.btStart_St2.setDisabled(False)
            self.btStop_St2.setDisabled(True)
            self.lblSt2RunState.setStyleSheet(self.StatuslblStyleSheet("RED"))
        elif stationId == "3":
            self.btStart_St3.setDisabled(False)
            self.btStop_St3.setDisabled(True)
            self.lblSt3RunState.setStyleSheet(self.StatuslblStyleSheet("RED"))
        else:
            raise ValueError

    def StatuslblStyleSheet(self, color):
        if color == "RED":
            return ("border: 1px;\n" 
                    "border-radius: 15px;\n"
                    "background-color: rgb(255, 0, 0);")
        elif color == "GREEN":
            return ("border: 1px;\n" 
                    "border-radius: 15px;\n"
                    "background-color: rgb(0, 255, 0);")
        else:
            raise AttributeError
    
    @pyqtSlot()
    def btPathSelect_Clicked(self):
        dialog = QtWidgets.QFileDialog(self)
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly, True)
        dialog.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, True)
        dialog.setDirectory("/home/piotr/pendrive/")

        if dialog.exec_():
            d = dialog.selectedFiles()
            if len(d) > 0:
                self.lEditFileName.setText(d[0])

    @pyqtSlot()
    def btStart_Clicked(self):
        btn = QObject.sender(self)
        if btn:
            if self.lEditFileName.text() == "":
                self.btPathSelect_Clicked()
            btn.setDisabled(True)
            btnName = btn.objectName()
            st = None
            if btnName == "btStart_St1":
                self.btStop_St1.setDisabled(False)
                self.btDischarge_St1.setDisabled(True)
                self.btFill_St1.setDisabled(True)
                self.lblSt1RunState.setStyleSheet(self.StatuslblStyleSheet("GREEN"))
                self.st1ReportName = self.lEditFileName.text() + \
                                     datetime.datetime.now().strftime("/ST1_%y_%m_%d_%H_%M.txt")
                st = self.st1
            elif btnName == "btStart_St2":
                self.btStop_St2.setDisabled(False)
                self.btDischarge_St2.setDisabled(True)
                self.btFill_St2.setDisabled(True)
                self.st2ReportName = self.lEditFileName.text() + \
                                     datetime.datetime.now().strftime("/ST2_%y_%m_%d_%H_%M.txt")
                self.lblSt2RunState.setStyleSheet(self.StatuslblStyleSheet("GREEN"))
                st = self.st2
            elif btnName == "btStart_St3":
                self.btStop_St3.setDisabled(False)
                self.btDischarge_St3.setDisabled(True)
                self.btFill_St3.setDisabled(True)
                self.st3ReportName = self.lEditFileName.text() + \
                                     datetime.datetime.now().strftime("/ST3_%y_%m_%d_%H_%M.txt")
                self.lblSt3RunState.setStyleSheet(self.StatuslblStyleSheet("GREEN"))
                st = self.st3
            
            st.setTestParams(int(self.sBoxCycleCounter.value()),
                             int(self.sBoxFillTime.value()),
                             60 * int(self.sBoxInFluidTime.value()),
                             int(self.sBoxDischargeTime.value()),
                             60 * int(self.sBoxInAirTime.value()) )
            st.start()                

    @pyqtSlot()
    def btStop_Clicked(self):
        btn = QObject.sender(self)
        if btn:
            btn.setDisabled(True)
            btnName = btn.objectName()
            st = None
            if btnName == "btStop_St1":
                self.btStart_St1.setDisabled(False)
                self.btDischarge_St1.setDisabled(False)
                self.btFill_St1.setDisabled(False)
                self.lblSt1RunState.setStyleSheet(self.StatuslblStyleSheet("RED"))
                st = self.st1
            elif btnName == "btStop_St2":
                self.btStart_St2.setDisabled(False)
                self.btDischarge_St2.setDisabled(False)
                self.btFill_St2.setDisabled(False)
                self.lblSt2RunState.setStyleSheet(self.StatuslblStyleSheet("RED"))
                st = self.st2
            elif btnName == "btStop_St3":
                self.btStart_St3.setDisabled(False)
                self.btDischarge_St3.setDisabled(False)
                self.btFill_St3.setDisabled(False)
                self.lblSt3RunState.setStyleSheet(self.StatuslblStyleSheet("RED"))
                st = self.st3

            st.stop()

    @pyqtSlot()
    def btFill_Pressed(self):
        btn = QObject.sender(self)
        if btn:
            btnName = btn.objectName()
            st = None
            if btnName == "btFill_St1":   st = self.st1
            elif btnName == "btFill_St2": st = self.st2
            elif btnName == "btFill_St3": st = self.st3

            st.setPump(pS.FILL)

    @pyqtSlot()
    def btFill_Released(self):
        btn = QObject.sender(self)
        if btn:
            btnName = btn.objectName()
            st = None
            if btnName == "btFill_St1":   st = self.st1
            elif btnName == "btFill_St2": st = self.st2
            elif btnName == "btFill_St3": st = self.st3

            st.setPump(pS.STOP)

    @pyqtSlot()
    def btDischarge_Pressed(self):
        btn = QObject.sender(self)
        if btn:
            btnName = btn.objectName()
            st = None
            if btnName == "btDischarge_St1":   st = self.st1
            elif btnName == "btDischarge_St2": st = self.st2
            elif btnName == "btDischarge_St3": st = self.st3

            st.setPump(pS.DISCHARGE)

    @pyqtSlot()
    def btDischarge_Released(self):
        btn = QObject.sender(self)
        if btn:
            btnName = btn.objectName()
            st = None
            if btnName == "btDischarge_St1":   st = self.st1
            elif btnName == "btDischarge_St2": st = self.st2
            elif btnName == "btDischarge_St3": st = self.st3

            st.setPump(pS.STOP)

    @pyqtSlot()
    def pBtnClearLogClicked(self):
        self.logView.clear()
    
    ### Stations timers slots
    @pyqtSlot()
    def st1_ioTimerCallback(self):
        self.st1.ioTimerCallback()

    @pyqtSlot()
    def st1_cycleTimerCallback(self):
        self.st1.cycleTimerCallback()

    @pyqtSlot()
    def st2_ioTimerCallback(self):
        self.st2.ioTimerCallback()

    @pyqtSlot()
    def st2_cycleTimerCallback(self):
        self.st2.cycleTimerCallback()

    @pyqtSlot()
    def st3_ioTimerCallback(self):
        self.st3.ioTimerCallback()

    @pyqtSlot()
    def st3_cycleTimerCallback(self):
        self.st3.cycleTimerCallback()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
    GPIO.cleanup()
