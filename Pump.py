from datetime import datetime


class Pump:
    def __init__(self, id):
        self.id = id
        self.isPumpOn = False
        self.history = []
        self.currentLog = None

    def startTimer(self):
        if(self.isPumpOn == False):
            currentTime = datetime.now()
            self.startTime = currentTime
            self.currentLog = HistoryItem(startTime=currentTime)
            self.isPumpOn = True
        else:
            print(f"Pump: {self.id} is already on")

    def stopTimer(self):
        if(self.isPumpOn == True):
            currentTime = datetime.now()
            self.endTime = currentTime
            self.currentLog.endTime = currentTime
            self.history.append(self.currentLog)
            self.currentLog = None
            self.isPumpOn = False
        else:
            print(f"Pump: {self.id} is already off")


class HistoryItem:
    def __init__(self, startTime=None, endTime=None):
        self.startTime = startTime
        self.endTime = endTime
