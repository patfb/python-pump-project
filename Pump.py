from datetime import datetime


class Pump:
    def __init__(self, id):
        self.id = id
        self.isPumpOn = False
        self.history = []

    def startTimer(self):
        if(self.isPumpOn == False):
            currentTime = datetime.now()
            self.history.append(HistoryItem(startTime=currentTime))
            self.isPumpOn = True
        else:
            print(f"Pump: {self.id} is already on")

    def stopTimer(self):
        if(self.isPumpOn == True):
            currentTime = datetime.now()
            self.history[-1].endTime = currentTime
            self.isPumpOn = False
        else:
            print(f"Pump: {self.id} is already off")

    def printAllLogs(self):
        for item in self.history:
            print(f"startTime: {item.startTime} endTime: {item.endTime}")


class HistoryItem:
    def __init__(self, startTime=None, endTime=None):
        self.startTime = startTime
        self.endTime = endTime
