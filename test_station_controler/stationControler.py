import datetime
from PyQt5.QtCore import QTimer
from enum import Enum
import stub_Adafruit_BBIO.GPIO as GPIO

class stationInputs():

    STATE_OK = True
    STATE_NOK = False

    def __init__(self):
        self.sample1 = ""
        self.sample2 = ""
        self.sample3 = ""

class stationOutputs():
    def __init__(self):
        self.dirOut = ""
        self.runOut = ""

class TestState():
    UNKNOWN =   (0, "UNKNOWN")
    FILL =      (1, "NALEWANIE")
    IN_FLUID =  (2, "W CIECZY")
    DISCHARGE = (3, "WYLEWANIE")
    IN_AIR =    (4, "W POWIETRZU")

class PumpState():
    FILL = 0
    DISCHARGE = 1
    STOP = 2

class stationControler():

    def __init__(self, parent, stNo):
        self._parent = parent
        self._stationId = stNo
        self._inputs = stationInputs()
        self._outputs = stationOutputs()

        ### Test Params
        self._cycleToDo = 0
        self._fillTime = 0
        self._inFluidTime = 0
        self._dischargeTime = 0
        self._inAirTime = 0

        ### Test counters
        self._cyclesRemainig = 0
        self._fillTimeRemaining = 0
        self._inFluidTimeRemaing = 0
        self._dischargeTimeRemaining = 0
        self._inAirTimeRemaining = 0

        self._demagedSamples = list()
        self._allSamplesBroken = False

        self.state = TestState.UNKNOWN
        self._progressValue = 0

        self.In1StatusLabel = None
        self.In2StatusLabel = None
        self.In3StatusLabel = None
        self.StateLabel = None
        self.PhaseLabel = None
        self.ProgressBar = None
        self._writeLog = staticmethod(lambda: (""))
        self._writeReport = staticmethod(lambda: (""))
        self.endOfTestCallback = staticmethod(lambda: (""))

        self.initIos()

        self._ioTimer = QTimer(self._parent)
        self._ioTimer.setSingleShot(False)

        self._cycleTimer = QTimer(self._parent)
        self._cycleTimer.setSingleShot(True)

        ########## End of init ##################

    @property
    def State(self):
        return self.state

    @State.setter
    def State(self, newVal):
          self.state = newVal
          self.PhaseLabel.setText("Faza: {}".format(self.state[1]))

    @property
    def Cycle(self):
        return self._cyclesRemainig
    
    @Cycle.setter
    def Cycle(self, newVal):
        self._cyclesRemainig = newVal
        currentCycle = self._cycleToDo - self._cyclesRemainig
        self.StateLabel.setText("Cykl: {}".format(currentCycle))

    @property
    def Progress(self):
        return self._progressValue

    @Progress.setter
    def Progress(self, newVal):
        self._progressValue = newVal
        self.ProgressBar.setValue(self._progressValue)

    def initIos(self):
        GPIO.setup(self._inputs.sample1, GPIO.IN)
        GPIO.setup(self._inputs.sample2, GPIO.IN)
        GPIO.setup(self._inputs.sample3, GPIO.IN)        

        GPIO.setup(self._outputs.runOut, GPIO.OUT)
        GPIO.setup(self._outputs.dirOut, GPIO.OUT)       

        GPIO.output(self._outputs.runOut, GPIO.LOW)
        GPIO.output(self._outputs.dirOut, GPIO.LOW)

    def start(self):
        self._writeReport(self._stationId,
                          "ROZPOCZETO TEST\n"
                          "ILOSC CYKLI = {}\n"
                          "CZAS NALEWANIA = {} s\n"
                          "CZAS W CIECZY = {} m\n"
                          "CZAS WYLEWANIA = {} s\n"
                          "CZAS W POWIETRZU = {} m\n".format(self._cyclesRemainig,
                                                            self._fillTimeRemaining,
                                                            self._inFluidTimeRemaing,
                                                            self._dischargeTimeRemaining,
                                                            self._inAirTimeRemaining))
        self._writeLog("Notify", "St.{} Rozpoczeto cykl testowy.".format(self._stationId))
        self._allSamplesBroken = False
        self._cycleTimer.start(0) # Kick the timer and let him take control

    def stop(self):
        self.setPump(PumpState.STOP)
        self._cycleTimer.stop()
        self._state = TestState.UNKNOWN

    def setTestParams(self, cyc, f, iF, dis, iA):
        self._cycleToDo = cyc
        self._cyclesRemainig = cyc
        self._fillTime = f
        self._fillTimeRemaining = f
        self._inFluidTime = iF
        self._inFluidTimeRemaing = iF
        self._dischargeTime = dis
        self._dischargeTimeRemaining = dis
        self._inAirTime = iA
        self._inAirTimeRemaining = iA

    def processStateUnknown(self):
        self._cycleTimer.start(1000)
        self.State = TestState.FILL
        self.Cycle = self._cycleToDo
        self.Cycle -= 1
        self.setPump(PumpState.FILL)

    def processStateFill(self):        
        self._cycleTimer.start(1000)
        if (self._fillTimeRemaining > 0 ):
            self._fillTimeRemaining -= 1 
            self._inFluidTimeRemaing -= 1
            self.Progress = self.getProgressPercent(self._fillTime, self._fillTimeRemaining)            
        else:
            self.setPump(PumpState.STOP)
            self._inFluidTimeRemaing -= 1
            self.State = TestState.IN_FLUID
            self.Progress = self.getProgressPercent(self._inFluidTime, self._inFluidTimeRemaing)

    def processStateInFluid(self):
        self._cycleTimer.start(1000)
        if (self._inFluidTimeRemaing > 0):
            self._inFluidTimeRemaing -= 1
            self.Progress = self.getProgressPercent(self._inFluidTime, self._inFluidTimeRemaing)
        else:
            self.setPump(PumpState.DISCHARGE)
            self.State = TestState.DISCHARGE

    def processStateDischarge(self):
        self._cycleTimer.start(1000)
        if self._allSamplesBroken: self.setPump(PumpState.DISCHARGE)
        if (self._dischargeTimeRemaining > 0):
            self._dischargeTimeRemaining -= 1
            self._inAirTimeRemaining -= 1
            self.Progress = self.getProgressPercent(self._dischargeTime, self._dischargeTimeRemaining)
        else:
            self.setPump(PumpState.STOP)
            self._inAirTimeRemaining -= 1
            self.State = TestState.IN_AIR
            self.Progress = self.getProgressPercent(self._inAirTime, self._inAirTimeRemaining)        
    
    def processStateInAir(self):
        if (self._inAirTimeRemaining > 0 and not self._allSamplesBroken):
            self._cycleTimer.start(1000)
            self._inAirTimeRemaining -= 1
            self.Progress = self.getProgressPercent(self._inAirTime, self._inAirTimeRemaining)            
        else:
            ### End of test cycle
            if (self._cyclesRemainig > 0 and not self._allSamplesBroken):
                ### Stil some test to do
                self.Cycle -= 1
                self._cycleTimer.start(1000)
                self.setPump(PumpState.FILL)
                self.State = TestState.FILL
                self.Progress = 0
                ### Start the cycle from the begining
                self._fillTimeRemaining = self._fillTime
                self._inFluidTimeRemaing = self._inFluidTime
                self._dischargeTimeRemaining = self._dischargeTime
                self._inAirTimeRemaining = self._inAirTime
            else:
                ### End of test
                self.StateLabel.setText("Cykl:")
                self.PhaseLabel.setText("Faza:")
                self.ProgressBar.setValue(0)
                self.endOfTestCallback(str(self._stationId))
                ### TODO: write report

    ### Callback method for IO polling timer
    def ioTimerCallback(self):
        In1 = GPIO.input(self._inputs.sample1)
        if In1 == stationInputs.STATE_OK:
            self.In1StatusLabel.setStyleSheet(self.lblStyleSheet("GREEN"))
            if self._inputs.sample1 in self._demagedSamples:
                self._demagedSamples.remove(self._inputs.sample1)
        else:
            if self._inputs.sample1 not in self._demagedSamples:
                self._demagedSamples.append(self._inputs.sample1)
                self._writeLog("Alert", "St.{} Probka 1 zerwana".format(self._stationId))
            self.In1StatusLabel.setStyleSheet(self.lblStyleSheet("RED"))

        In2 = GPIO.input(self._inputs.sample2)
        if In2 == stationInputs.STATE_OK:
            self.In2StatusLabel.setStyleSheet(self.lblStyleSheet("GREEN"))
            if self._inputs.sample2 in self._demagedSamples:
                self._demagedSamples.remove(self._inputs.sample2)
        else:
            if self._inputs.sample2 not in self._demagedSamples:
                self._demagedSamples.append(self._inputs.sample2)
                self._writeLog("Alert", "St.{} Probka 2 zerwana".format(self._stationId))
            self.In2StatusLabel.setStyleSheet(self.lblStyleSheet("RED"))

        In3 = GPIO.input(self._inputs.sample3)
        if In3 == stationInputs.STATE_OK:
            self.In3StatusLabel.setStyleSheet(self.lblStyleSheet("GREEN"))
            if self._inputs.sample3 in self._demagedSamples:
                self._demagedSamples.remove(self._inputs.sample3)
        else:
            if self._inputs.sample3 not in self._demagedSamples:
                self._demagedSamples.append(self._inputs.sample3)
                self._writeLog("Alert", "St.{} Probka 3 zerwana".format(self._stationId))
            self.In3StatusLabel.setStyleSheet(self.lblStyleSheet("RED"))

        if (In1 == stationInputs.STATE_NOK and
            In2 == stationInputs.STATE_NOK and
            In3 == stationInputs.STATE_NOK and not
            self._allSamplesBroken):
            self._allSamplesBroken = True
            self.State = TestState.DISCHARGE
            self._cycleTimer.start(0)  ### Kick the timer

    ### Callback method for cycle timer
    def cycleTimerCallback(self):
        if (self.state == TestState.UNKNOWN):
            self.processStateUnknown()
        elif (self.state == TestState.FILL):
            self.processStateFill()
        elif (self.state == TestState.IN_FLUID):
            self.processStateInFluid()
        elif (self.state == TestState.DISCHARGE):
            self.processStateDischarge()
        elif (self.state == TestState.IN_AIR):
            self.processStateInAir()

    def setPump(self, state):
        if state == PumpState.STOP:
            GPIO.output(self._outputs.runOut, GPIO.LOW)
            GPIO.output(self._outputs.dirOut, GPIO.LOW)
        elif state == PumpState.FILL:
            GPIO.output(self._outputs.dirOut, GPIO.HIGH)
            GPIO.output(self._outputs.runOut, GPIO.HIGH)
        elif state == PumpState.DISCHARGE:
            GPIO.output(self._outputs.dirOut, GPIO.LOW)
            GPIO.output(self._outputs.runOut, GPIO.HIGH)
        else:
            raise ValueError()

    ### Utils functions -should not be here in fact
    ### TODO: find a better place for this methods
    def getProgressPercent(self, total, current):
        return int( (float(total) - float(current)) / float(total) * 100.0)
    def lblStyleSheet(self, color):
        if color == "RED":
            return ("border: 1px;\n" 
                    "border-radius: 10px;\n"
                    "background-color: rgb(255, 0, 0);")
        elif color == "GREEN":
            return ("border: 1px;\n" 
                    "border-radius: 10px;\n"
                    "background-color: rgb(0, 255, 0);")
        else:
            raise AttributeError
