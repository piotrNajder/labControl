import sys
import os.path
import shutil
from enum import Enum
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtCore import QTimer
from controlerUI import Ui_MainWindow
import time

class TestState(Enum):
    UNKNOWN = 0
    FILL = 1
    IN_FLUID = 2
    DISCHARGE = 3
    IN_AIR = 4

class Main(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        self._currentState = TestState.UNKNOWN
        self._cyclesRemainig = 0
        self._fillTimeRemaining = 0
        self._inFluidTimeRemaing = 0
        self._dischargeTimeRemaining = 0
        self._inAirTimeRemaining = 0

        self.tBtnFileSelect.clicked.connect(lambda: self.tBtnFileSelect_Clicked())
        self.btStart.clicked.connect(lambda: self.pBtnRun_Clicked())
        self.btnStop.clicked.connect(lambda: self.pBtnStop_Clicked())

        self.pBtnStation1.clicked.connect(lambda: self.btnStation1Clicked())
        self.pBtnStation2.clicked.connect(lambda: self.btnStation2Clicked())
        self.pBtnStation3.clicked.connect(lambda: self.btnStation3Clicked())

        self.pBtnFill.clicked.connect(lambda: self.pBtnFillClicked())
        self.pBtnInFluid.clicked.connect(lambda: self.pBtnInFluidClicked())
        self.pBtnDischarge.clicked.connect(lambda: self.pBtnDischargedClicked())
        self.pBtnInAir.clicked.connect(lambda: self.pBtnInAirClicked())
        self.pBtnCycleCounter.clicked.connect(lambda: self.pBtnCycleCounterClicked())
        self.btnEnd.clicked.connect(lambda: self.btnEndClicked())

        self._ioPollTimer = QTimer(self)
        self._ioPollTimer.setSingleShot(False)
        self._ioPollTimer.timeout.connect(self.ioTimerTimout)        
        self._ioPollTimer.start(10)

        self._cycleTimer = QTimer(self)
        self._cycleTimer.setSingleShot(True)
        self._cycleTimer.timeout.connect(self.cycleTimerTimeout)

    def startFillPump(self):
        pass

    def stopFillPump(self):
        pass

    def startDischargePump(self):
        pass

    def stopDischargePump(self):
        pass

    @pyqtSlot()
    def tBtnFileSelect_Clicked(self):       
        options = QtWidgets.QFileDialog.Options() 
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Choose an image file...", "", "Image Files (*.jpg *.jpeg *.png)")

        self.lEditFileName.setText(fileName)
        imgOrgi = QtGui.QImage(fileName)
        self.imgDisplayed = imgOrgi.scaled(710, 395, QtCore.Qt.KeepAspectRatio)
        self.lImageView.setPixmap(QtGui.QPixmap.fromImage(self.imgDisplayed))
        print("Opened file: {}".format(fileName))

    @pyqtSlot()
    def pBtnRun_Clicked(self):
        self.btnStop.setDisabled(False)
        self.btStart.setDisabled(True)
        self._cyclesRemainig = int(self.sBoxCycleCounter.value())
        self._fillTimeRemaining = int(self.sBoxFillTime.value())
        self._inFluidTimeRemaing = 60 * int(self.sBoxInFluidTime.value())
        self._dischargeTimeRemaining = int(self.sBoxDischargeTime.value())
        self._inAirTimeRemaining = 60 * int(self.sBoxInAirTime.value())
        self._cycleTimer.start(0) # Kick the timer and let him take control

    @pyqtSlot()
    def pBtnStop_Clicked(self):
        self.btnStop.setDisabled(True)
        self.btStart.setDisabled(False)
        self._cycleTimer.stop()
        self._currentState = TestState.UNKNOWN

    @pyqtSlot()
    def closeEvent(self, evnt):
        pass

    @pyqtSlot()
    def ioTimerTimout(self):
        # Reads the samples input and updates the controls in GUI
        pass

    @pyqtSlot()
    def cycleTimerTimeout(self):
        if (self._currentState == TestState.UNKNOWN):
            ### Initial state of app
            ### Need to transit to FILL state
            ### start the filling process ( control IO )
            self._currentState = TestState.FILL
            currentCycle = int(self.sBoxCycleCounter.value()) - self._cyclesRemainig + 1 
            self.lblActualCycle.setText("Aktualny cykl: {}".format(currentCycle))
            self.lblActualState.setText("Stan próbki: NALEWANIE")
            self.startFillPump()
            self._cycleTimer.start(1000)

        elif (self._currentState == TestState.FILL):
            if (self._fillTimeRemaining > 0 ):
                self._fillTimeRemaining -= 1 
                self._inFluidTimeRemaing -= 1
                progressValue = self.getProgressPercent(int(self.sBoxFillTime.value()),
                                                            self._fillTimeRemaining)
                self.pBarStateProgress.setValue(progressValue)
            else:
                self.stopFillPump()
                self._inFluidTimeRemaing -= 1
                self._currentState = TestState.IN_FLUID
                progressValue = self.getProgressPercent(60 * int(self.sBoxInFluidTime.value()),
                                                            self._inFluidTimeRemaing)
                self.pBarStateProgress.setValue(0)
                self.pBarStateProgress.setValue(progressValue)
                self.lblActualState.setText("Stan próbki: W CIECZY")
            self._cycleTimer.start(1000)

        elif (self._currentState == TestState.IN_FLUID):
            if (self._inFluidTimeRemaing > 0):
                self._inFluidTimeRemaing -= 1
                progressValue = self.getProgressPercent(60 * int(self.sBoxInFluidTime.value()),
                                                        self._inFluidTimeRemaing)
                self.pBarStateProgress.setValue(progressValue)
            else:
                self.startDischargePump()
                self._currentState = TestState.DISCHARGE
                self.lblActualState.setText("Stan próbki: WYLEWANIE")
                self.pBarStateProgress.setValue(0)
            self._cycleTimer.start(1000)

        elif (self._currentState == TestState.DISCHARGE):
            if (self._dischargeTimeRemaining > 0):
                self._dischargeTimeRemaining -= 1
                self._inAirTimeRemaining -= 1
                progressValue = self.getProgressPercent(int(self.sBoxDischargeTime.value()),
                                                            self._dischargeTimeRemaining)
                self.pBarStateProgress.setValue(progressValue)
            else:
                self.stopDischargePump()
                self._inAirTimeRemaining -= 1
                self._currentState = TestState.IN_AIR
                self.lblActualState.setText("Stan próbki: W POWETRZU")
                progressValue = self.getProgressPercent(60 * int(self.sBoxInAirTime.value()),
                                                        self._inAirTimeRemaining)
                self.pBarStateProgress.setValue(0)
                self.pBarStateProgress.setValue(progressValue)
            self._cycleTimer.start(1000)

        elif (self._currentState == TestState.IN_AIR):
            if (self._inAirTimeRemaining > 0):
                self._inAirTimeRemaining -= 1
                progressValue = self.getProgressPercent(60 * int(self.sBoxInAirTime.value()),
                                                            self._inAirTimeRemaining)
                self.pBarStateProgress.setValue(progressValue)
                self._cycleTimer.start(1000)
            else:
                ### End of test cycle
                if (self._cyclesRemainig > 0):
                    ### Stil some test to do
                    self._cyclesRemainig -= 1
                    currentCycle = int(self.sBoxCycleCounter.value()) - self._cyclesRemainig + 1 
                    self.pBarStateProgress.setValue(0)
                    self.lblActualCycle.setText("Aktualny cykl: {}".format(currentCycle))
                    self.lblActualState.setText("Stan próbki: NALEWANIE")
                    ### Start the cycle from the begining
                    self._fillTimeRemaining = int(self.sBoxFillTime.value())
                    self._inFluidTimeRemaing = 60 * int(self.sBoxInFluidTime.value())
                    self._dischargeTimeRemaining = int(self.sBoxDischargeTime.value())
                    self._inAirTimeRemaining = 60 * int(self.sBoxInAirTime.value())
                    self._currentState = TestState.FILL
                    self.startFillPump()
                    self._cycleTimer.start(1000)
                else:
                    ### End of test
                    pass
                    ### TODO: write report


    @pyqtSlot()
    def btnStation1Clicked(self):
        if self.gbStation1.isChecked():
            self.gbStation1.setChecked(False)
        else:
            self.gbStation1.setChecked(True)

    @pyqtSlot()
    def btnStation2Clicked(self):
        if self.gbStation2.isChecked():
            self.gbStation2.setChecked(False)
        else:
            self.gbStation2.setChecked(True)

    @pyqtSlot()
    def btnStation3Clicked(self):
        if self.gbStation3.isChecked():
            self.gbStation3.setChecked(False)
        else:
            self.gbStation3.setChecked(True)

    @pyqtSlot()
    def pBtnFillClicked(self):
        self.sBoxFillTime.setFocus()

    @pyqtSlot()
    def pBtnInFluidClicked(self):
        self.sBoxInFluidTime.setFocus()

    @pyqtSlot()
    def pBtnDischargedClicked(self):
        self.sBoxDischargeTime.setFocus()

    @pyqtSlot()
    def pBtnInAirClicked(self):
        self.sBoxInAirTime.setFocus()

    @pyqtSlot()
    def pBtnCycleCounterClicked(self):
        self.sBoxCycleCounter.setFocus()

    @pyqtSlot()
    def btnEndClicked(self):
        self.close()

    def getProgressPercent(self, total, current):
        actVal = float(total) - float(current)
        return int( actVal / float(total) * 100.0)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Main()
    app.setStyle(QtGui.QStyleFactory.create("Windows"))
    window.show()
    sys.exit(app.exec_())    