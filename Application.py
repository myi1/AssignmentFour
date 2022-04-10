class Application:

    def __init__(self):
        self._listSensors = []
        self._numSensors = 0

    def getListSensors(self):
        return self._listSensors

    def getNumSensors(self):
        return self._numSensors

    def setListSensors(self, newListSensors):
        self._listSensors = newListSensors

    def setNumSensors(self, newNumSensors):
        self._numSensors = newNumSensors

    def askNumSensors(self):
        validInput = False
        while validInput is not True:
            try:
                numSensors = int(input("Enter the number of sensors: "))
            except:
                print("This is an invalid entry for the number of sensors!")
            else:
                self.setNumSensors = numSensors
                validInput = True

    def askSensorID(self):
        validInput = False
        while validInput is not True:
            try:
                sensorID = input(
                    "_*__*__*__*__*__*__*__*__*__*_\nEnter the Sensor Id: ")
                if sensorID.isalpha():
                    validInput = True
                    return sensorID
                else:
                    raise TypeError
            except:
                print("This is an invalid entry for sensor Id!")

    def getNeighbors(self):
        validInput = False
        while validInput is not True:
            try:
                numNeighbors = int(input('Enter the number of neighbours: '))
            except:
                print(
                    "This is an invalid entry for the neighbour's name and/or distance!")
            else:
                validInput = True
                return numNeighbors

    def getDistance(self, sensorID):
        validInput = False
        while validInput is not True:
            try:
                distance = int(
                    input('Enter the neighbor for Sensor {0}: '.format(sensorID)))
            except:
                print(
                    'This is an invalid entry for the neighbour’s name and/or distance!')
            else:
                validInput = True
                return distance

    def getOxygen(self):
        validInput = False
        while validInput is not True:
            try:
                oxygenLevel = int(input('Enter the Oxygen level in %: '))
            except:
                print('This is an invalid entry for the oxygen level!')
            else:
                validInput = True
                return oxygenLevel

    def getTemp(self):
        validInput = False
        while validInput is not True:
            try:
                temp = int(input('Enter the temperature measurement: '))
            except:
                print('This is an invalid entry for the temperature!')
            else:
                validInput = True
                return temp


App = Application()
App.getTemp()
