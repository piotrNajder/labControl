import sys
import os.path
import shutil
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot, QTimer
from controlerUI import Ui_MainWindow, _fromUtf8
import Adafruit_BBIO.GPIO as GPIO
import time

class TestState():
    UNKNOWN = (0, "UNKNOWN")
    FILL = (1, "NALEWANIE")
    IN_FLUID = (2, "W CIECZY")
    DISCHARGE = (3, "WYLEWANIE")
    IN_AIR = (4, "W POWIETRZU")

class PumpState():
    FILL = 0
    DISCHARGE = 1
    STOP = 2

class StationState():
    USE = 0
    NOT_USE = 1
    ALL_DOWN = 2

class AppState():
    RUNNING = 0
    STOPED = 1

class ControlerIos():
    st1Smpl1 = "GPIO0_1"
    st1Smpl2 = "GPIO0_2"
    st1Smpl3 = "GPIO0_3"
    st2Smpl1 = "GPIO0_4"
    st2Smpl2 = "GPIO0_5"
    st2Smpl3 = "GPIO0_6"
    st3Smpl1 = "GPIO0_7"
    st3Smpl2 = "GPIO0_8"
    st3Smpl3 = "GPIO0_9"

    st1PumpStart = "GPIO0_10"
    st1PumpDir = "GPIO0_11"
    st2PumpStart = "GPIO0_12"
    st2PumpDir = "GPIO0_13"
    st3PumpStart = "GPIO0_14"
    st3PumpDir = "GPIO0_15"

    STATE_OK = True
    STATE_NOK = False

    @staticmethod
    def initIos():
        GPIO.setup(ControlerIos.st1Smpl1, GPIO.IN)
        GPIO.setup(ControlerIos.st1Smpl2, GPIO.IN)
        GPIO.setup(ControlerIos.st1Smpl3, GPIO.IN)
        GPIO.setup(ControlerIos.st2Smpl1, GPIO.IN)
        GPIO.setup(ControlerIos.st2Smpl2, GPIO.IN)
        GPIO.setup(ControlerIos.st2Smpl3, GPIO.IN)
        GPIO.setup(ControlerIos.st3Smpl1, GPIO.IN)
        GPIO.setup(ControlerIos.st3Smpl2, GPIO.IN)
        GPIO.setup(ControlerIos.st3Smpl3, GPIO.IN)

        GPIO.setup(ControlerIos.st1PumpStart, GPIO.OUT)
        GPIO.setup(ControlerIos.st1PumpDir, GPIO.OUT)
        GPIO.setup(ControlerIos.st2PumpStart, GPIO.OUT)
        GPIO.setup(ControlerIos.st2PumpDir, GPIO.OUT)
        GPIO.setup(ControlerIos.st3PumpStart, GPIO.OUT)
        GPIO.setup(ControlerIos.st3PumpDir, GPIO.OUT)

        GPIO.output(ControlerIos.st1PumpStart, GPIO.LOW)
        GPIO.output(ControlerIos.st1PumpDir, GPIO.LOW)
        GPIO.output(ControlerIos.st2PumpStart, GPIO.LOW)
        GPIO.output(ControlerIos.st2PumpDir, GPIO.LOW)
        GPIO.output(ControlerIos.st3PumpStart, GPIO.LOW)
        GPIO.output(ControlerIos.st3PumpDir, GPIO.LOW)

    @staticmethod
    def sampleState(station, sample):
        if station == 1:
            if sample == 1:
                return GPIO.input(ControlerIos.st1Smpl1)
            elif sample == 2:
                return GPIO.input(ControlerIos.st1Smpl2)
            elif sample == 3:
                return GPIO.input(ControlerIos.st1Smpl3)
            else:
                pass 
        elif station == 2:
            if sample == 1:
                return GPIO.input(ControlerIos.st2Smpl1)
            elif sample == 2:
                return GPIO.input(ControlerIos.st2Smpl2)
            elif sample == 3:
                return GPIO.input(ControlerIos.st2Smpl3)
            else:
                pass 
        elif station == 3:
            if sample == 1:
                return GPIO.input(ControlerIos.st3Smpl1)
            elif sample == 2:
                return GPIO.input(ControlerIos.st3Smpl2)
            elif sample == 3:
                return GPIO.input(ControlerIos.st3Smpl3)
            else:
                pass 
        else:
            pass

    @staticmethod
    def setPump(station, state):
        if station == 1:
            if state == PumpState.STOP:
                GPIO.output(ControlerIos.st1PumpStart, GPIO.LOW)
                GPIO.output(ControlerIos.st1PumpDir, GPIO.LOW)
            elif state == PumpState.FILL:
                GPIO.output(ControlerIos.st1PumpDir, GPIO.HIGH)
                GPIO.output(ControlerIos.st1PumpStart, GPIO.HIGH)
            elif state == PumpState.DISCHARGE:
                GPIO.output(ControlerIos.st1PumpDir, GPIO.LOW)
                GPIO.output(ControlerIos.st1PumpStart, GPIO.HIGH)
            else:
                pass
        elif station == 2:
            if state == PumpState.STOP:
                GPIO.output(ControlerIos.st2PumpStart, GPIO.LOW)
                GPIO.output(ControlerIos.st2PumpDir, GPIO.LOW)
            elif state == PumpState.FILL:
                GPIO.output(ControlerIos.st2PumpDir, GPIO.HIGH)
                GPIO.output(ControlerIos.st2PumpStart, GPIO.HIGH)
            elif state == PumpState.DISCHARGE:
                GPIO.output(ControlerIos.st2PumpDir, GPIO.LOW)
                GPIO.output(ControlerIos.st2PumpStart, GPIO.HIGH)
            else:
                pass
        elif station == 3:
            if state == PumpState.STOP:
                GPIO.output(ControlerIos.st3PumpStart, GPIO.LOW)
                GPIO.output(ControlerIos.st3PumpDir, GPIO.LOW)
            elif state == PumpState.FILL:
                GPIO.output(ControlerIos.st3PumpDir, GPIO.HIGH)
                GPIO.output(ControlerIos.st3PumpStart, GPIO.HIGH)
            elif state == PumpState.DISCHARGE:
                GPIO.output(ControlerIos.st3PumpDir, GPIO.LOW)
                GPIO.output(ControlerIos.st3PumpStart, GPIO.HIGH)
            else:
                pass
        else:
            pass
    

class Main(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        ControlerIos.initIos()
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.initControlsCallbacks()

        self._currentState = TestState.UNKNOWN
        self._cyclesRemainig = 0
        self._progressValue = 0
        self._fillTimeRemaining = 0
        self._inFluidTimeRemaing = 0
        self._dischargeTimeRemaining = 0
        self._inAirTimeRemaining = 0

        self._st1State = StationState.NOT_USE
        self._st2State = StationState.NOT_USE
        self._st3State = StationState.NOT_USE

        self._appState = AppState.STOPED

        self.initTimers()


    def initTimers(self):
        self._ioPollTimer = QTimer(self)
        self._ioPollTimer.setSingleShot(False)
        self._ioPollTimer.timeout.connect(self.ioTimerTimout)        
        self._ioPollTimer.start(20)

        self._cycleTimer = QTimer(self)
        self._cycleTimer.setSingleShot(True)
        self._cycleTimer.timeout.connect(self.cycleTimerTimeout)

    def initControlsCallbacks(self):
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

    @property
    def State(self):
        return self._currentState

    @State.setter
    def State(self, newVal):
          self._currentState = newVal
          self.lblActualState.setText("Stan próbki: {}".format(self._currentState[1]))

    @property
    def Cycle(self):
        return self._cyclesRemainig
    
    @Cycle.setter
    def Cycle(self, newVal):
        self._cyclesRemainig = newVal
        currentCycle = int(self.sBoxCycleCounter.value()) - self._cyclesRemainig + 1 
        self.lblActualCycle.setText("Aktualny cykl: {}".format(currentCycle))

    @property
    def Progress(self):
        return self._progressValue

    @Progress.setter
    def Progress(self, newVal):
        self._progressValue = newVal
        self.pBarStateProgress.setValue(self._progressValue)

    def pumpControl(self, pumpState):        
        if self.gbStation1.isChecked():
            ControlerIos.setPump(1, pumpState)
        if self.gbStation2.isChecked():
            ControlerIos.setPump(2, pumpState)
        if self.gbStation3.isChecked():
            ControlerIos.setPump(3, pumpState)

    def processStateUnknown(self):
        self._cycleTimer.start(1000)
        self.State = TestState.FILL
        self.Cycle = int(self.sBoxCycleCounter.value())
        self.pumpControl(PumpState.FILL)

    def processStateFill(self):
        self._cycleTimer.start(1000)
        if (self._fillTimeRemaining > 0 ):
            self._fillTimeRemaining -= 1 
            self._inFluidTimeRemaing -= 1
            self.Progress = self.getProgressPercent(int(self.sBoxFillTime.value()), self._fillTimeRemaining)            
        else:
            self.pumpControl(PumpState.STOP)
            self._inFluidTimeRemaing -= 1
            self.State = TestState.IN_FLUID
            self.Progress = self.getProgressPercent(60 * int(self.sBoxInFluidTime.value()), self._inFluidTimeRemaing)

    def processStateInFluid(self):
        self._cycleTimer.start(1000)
        if (self._inFluidTimeRemaing > 0):
            self._inFluidTimeRemaing -= 1
            self.Progress = self.getProgressPercent(60 * int(self.sBoxInFluidTime.value()), self._inFluidTimeRemaing)
        else:
            self.pumpControl(PumpState.DISCHARGE)
            self.State = TestState.DISCHARGE

    def processStateDischarge(self):
        self._cycleTimer.start(1000)
        if (self._dischargeTimeRemaining > 0):
            self._dischargeTimeRemaining -= 1
            self._inAirTimeRemaining -= 1
            self.Progress = self.getProgressPercent(int(self.sBoxDischargeTime.value()), self._dischargeTimeRemaining)
        else:
            self.pumpControl(PumpState.STOP)
            self._inAirTimeRemaining -= 1
            self.State = TestState.IN_AIR
            self.Progress = self.getProgressPercent(60 * int(self.sBoxInAirTime.value()), self._inAirTimeRemaining)        
    
    def processStateInAir(self):
        if (self._inAirTimeRemaining > 0):
            self._cycleTimer.start(1000)
            self._inAirTimeRemaining -= 1
            self.Progress = self.getProgressPercent(60 * int(self.sBoxInAirTime.value()), self._inAirTimeRemaining)            
        else:
            ### End of test cycle
            if (self._cyclesRemainig > 0):
                ### Stil some test to do
                self._cycleTimer.start(1000)
                self.pumpControl(PumpState.FILL)
                self.Cycle -= 1
                self.State = TestState.FILL
                self.Progress = 0
                ### Start the cycle from the begining
                self._fillTimeRemaining = int(self.sBoxFillTime.value())
                self._inFluidTimeRemaing = 60 * int(self.sBoxInFluidTime.value())
                self._dischargeTimeRemaining = int(self.sBoxDischargeTime.value())
                self._inAirTimeRemaining = 60 * int(self.sBoxInAirTime.value())
            else:
                ### End of test
                pass
                ### TODO: write report

    @pyqtSlot()
    def tBtnFileSelect_Clicked(self):       
        options = QtWidgets.QFileDialog.Options() 
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Choose an image file...", "", "Image Files (*.jpg *.jpeg *.png)")

        self.lEditFileName.setText(fileName)

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
        if self.gbStation1.isChecked():
            In1 = ControlerIos.sampleState(1,1)
            In2 = ControlerIos.sampleState(1,2)
            In3 = ControlerIos.sampleState(1,3)

            if In1 == ControlerIos.STATE_OK:
                self.lblSt1Smpl1State.setStyleSheet(self.lblStyleSheet("GREEN"))
            else:
                self.lblSt1Smpl1State.setStyleSheet(self.lblStyleSheet("RED"))

            if In2 == ControlerIos.STATE_OK:
                self.lblSt1Smpl2State.setStyleSheet(self.lblStyleSheet("GREEN"))
            else:
                self.lblSt1Smpl2State.setStyleSheet(self.lblStyleSheet("RED"))

            if In3 == ControlerIos.STATE_OK:
                self.lblSt1Smp3State.setStyleSheet(self.lblStyleSheet("GREEN"))
            else:
                self.lblSt1Smp3State.setStyleSheet(self.lblStyleSheet("RED"))

            if (In1 == ControlerIos.STATE_NOK and
                In2 == ControlerIos.STATE_NOK and
                In3 == ControlerIos.STATE_NOK):
                ### SET station to DISCHARGE and leave it in IN_AIR
                pass
        
        if self.gbStation2.isChecked():
            In1 = ControlerIos.sampleState(2,1)
            In2 = ControlerIos.sampleState(2,2)
            In3 = ControlerIos.sampleState(2,3)

            if In1 == ControlerIos.STATE_OK:
                self.lblSt2Smpl1State.setStyleSheet(self.lblStyleSheet("GREEN"))
            else:
                self.lblSt2Smpl1State.setStyleSheet(self.lblStyleSheet("RED"))

            if In2 == ControlerIos.STATE_OK:
                self.lblSt2Smpl2State.setStyleSheet(self.lblStyleSheet("GREEN"))
            else:
                self.lblSt2Smpl2State.setStyleSheet(self.lblStyleSheet("RED"))

            if In3 == ControlerIos.STATE_OK:
                self.lblSt2Smp3State.setStyleSheet(self.lblStyleSheet("GREEN"))
            else:
                self.lblSt2Smp3State.setStyleSheet(self.lblStyleSheet("RED"))

            if (In1 == ControlerIos.STATE_NOK and
                In2 == ControlerIos.STATE_NOK and
                In3 == ControlerIos.STATE_NOK):
                ### SET station to DISCHARGE and leave it in IN_AIR
                pass    

        if self.gbStation3.isChecked():
            In1 = ControlerIos.sampleState(3,1)
            In2 = ControlerIos.sampleState(3,2)
            In3 = ControlerIos.sampleState(3,3)

            if In1 == ControlerIos.STATE_OK:
                self.lblSt3Smpl1State.setStyleSheet(self.lblStyleSheet("GREEN"))
            else:
                self.lblSt3Smpl1State.setStyleSheet(self.lblStyleSheet("RED"))

            if In2 == ControlerIos.STATE_OK:
                self.lblSt3Smpl2State.setStyleSheet(self.lblStyleSheet("GREEN"))
            else:
                self.lblSt3Smpl2State.setStyleSheet(self.lblStyleSheet("RED"))

            if In3 == ControlerIos.STATE_OK:
                self.lblSt3Smp3State.setStyleSheet(self.lblStyleSheet("GREEN"))
            else:
                self.lblSt3Smp3State.setStyleSheet(self.lblStyleSheet("RED"))

            if (In1 == ControlerIos.STATE_NOK and
                In2 == ControlerIos.STATE_NOK and
                In3 == ControlerIos.STATE_NOK):
                ### SET station to DISCHARGE and leave it in IN_AIR
                pass

    @pyqtSlot()
    def cycleTimerTimeout(self):
        if (self._currentState == TestState.UNKNOWN):
            self.processStateUnknown()
        elif (self._currentState == TestState.FILL):           
            self.processStateFill()
        elif (self._currentState == TestState.IN_FLUID):
            self.processStateFill()
        elif (self._currentState == TestState.DISCHARGE):
            self.processStateDischarge()
        elif (self._currentState == TestState.IN_AIR):
            self.processStateInAir()

    @pyqtSlot()
    def btnStation1Clicked(self):
        if self._appState != AppState.RUNNING:
            if self.gbStation1.isChecked():
                self.gbStation1.setChecked(False)
            else:
                self.gbStation1.setChecked(True)

    @pyqtSlot()
    def btnStation2Clicked(self):
        if self._appState != AppState.RUNNING:
            if self.gbStation2.isChecked():
                self.gbStation2.setChecked(False)
            else:
                self.gbStation2.setChecked(True)

    @pyqtSlot()
    def btnStation3Clicked(self):
        if self._appState != AppState.RUNNING:
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
        return int( (float(total) - float(current)) / float(total) * 100.0)

    def lblStyleSheet(self, color):
        if color == "RED":
            return _fromUtf8("border: 1px;\n" 
                             "border-radius: 10px;\n"
                             "background-color: rgb(255, 0, 0);")
        elif color == "GREEN":
            return _fromUtf8("border: 1px;\n" 
                             "border-radius: 10px;\n"
                             "background-color: rgb(0, 255, 0);")
        else:
            raise AttributeError

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Main()
    app.setStyle(QtGui.QStyleFactory.create("Windows"))
    window.show()
    sys.exit(app.exec_())
    GPIO.cleanup()