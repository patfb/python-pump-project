from datetime import datetime

# https://docs.python.org/3/tutorial/controlflow.html
# https://stackoverflow.com/questions/26002497/how-to-run-a-background-timer-in-python
# https://www.programiz.com/python-programming/datetime/current-time

def offerChoices(pumpState):
    if pumpState == "Y":
        print("Pump is on")
        startTime = datetime.now()
        print("current time is", startTime)

    elif pumpState == "N":
        print("Pump is not on")
    else:
        print("Invalid Response")

    if pumpState == "Y":
        isPumpStillOn = input("Is pump still on? Y/N: ")
        if isPumpStillOn == "Y":
            print("Pump is still on")
        elif isPumpStillOn == "N":
            print("Pump is off")
            endTime = datetime.now()
            print("current time is", endTime)
            print("Total time pump was on:", endTime-startTime)
        else:
            print("Invalid Response")


isPumpOn = input("Is pump on? Y/N: ")

offerChoices(isPumpOn)