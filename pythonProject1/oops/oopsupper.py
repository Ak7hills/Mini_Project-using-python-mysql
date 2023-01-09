class inputstring:
    def __init__(self):
        self.s=""
    def getstring(self):
        self.s=input("enter the string:")
    def printstring(self):
        print(self.s.upper())

a=inputstring()
a.getstring()
a.printstring()