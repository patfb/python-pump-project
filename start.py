from Pump import Pump


backyard = Pump("back")

print(f"Is pump on? {backyard.isPumpOn}")
backyard.startTimer()
print(f"Is pump on? {backyard.isPumpOn}")

input("stalling...")
backyard.stopTimer()

backyard.startTimer()
input("stalling again")
backyard.stopTimer()

print(f"Is pump on? {backyard.isPumpOn}")

print(f"Total number of start/end time pairs: {len(backyard.history)}")

print(backyard.printAllLogs())
