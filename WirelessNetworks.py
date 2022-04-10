from hashlib import new


class WirelessNetworks:

    def __init__(self):
        self._id: 0
        self._oxygenLevel = 0
        self._temperature = 0

    def getId(self):
        return self._id

    def getOxygenLevel(self):
        return self._oxygenLevel

    def getTemperature(self):
        return self._temperature

    def setId(self, newId):
        self._id = newId

    def setOxygenLevel(self, newOxygenLevel):
        self._oxygenLevel = newOxygenLevel

    def setTemperature(self, newTemperature):
        self._temperature = newTemperature

    def askSensorID(self):
        validInput = False
        while validInput is not True:
            try:
                sensorID = input(
                    "_*__*__*__*__*__*__*__*__*__*_\nEnter the Sensor Id: ")
                if sensorID.isalpha():
                    validInput = True
                    self.setId(sensorID)
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

    def getNeighborofSensor(self, sensorID):
        validInput = False
        while validInput is not True:
            try:
                neighbor = (
                    input('Enter the neighbor for Sensor {0}: '.format(sensorID)))

                if neighbor.isalpha():
                    validInput = True
                    return neighbor
                else:
                    raise TypeError
            except:
                print(
                    "This is an invalid entry for the neighbour's name and/or distance!")

    def getDistance(self, sensorID):
        validInput = False
        while validInput is not True:
            try:
                distance = int(
                    input('Enter the distance to {0}: '.format(sensorID)))
            except:
                print(
                    "This is an invalid entry for the neighbour's name and/or distance!")
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
                self.setOxygenLevel(oxygenLevel)
                validInput = True

    def getTemp(self):
        validInput = False
        while validInput is not True:
            try:
                temp = int(input('Enter the temperature measurement: '))
            except:
                print('This is an invalid entry for the temperature!')
            else:
                self.setTemperature(temp)
                validInput = True
