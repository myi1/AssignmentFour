from hashlib import new


class WirelessNetworks:
    # Static Variables
    ADHOC_Mode = 'ON'
    BRAND_NAME = 'Cisco'

    def __init__(self):
        self._id: 0
        self._oxygenLevel = 0
        self._temperature = 0
        self._neighborsList = []

    # Accessor Methods
    def getId(self):
        return self._id

    def getOxygenLevel(self):
        return self._oxygenLevel

    def getTemperature(self):
        return self._temperature

    def getNeighborsList(self):
        return self._neighborsList

    # Mutator Methods
    def setId(self, newId):
        self._id = newId

    def setOxygenLevel(self, newOxygenLevel):
        self._oxygenLevel = newOxygenLevel

    def setTemperature(self, newTemperature):
        self._temperature = newTemperature

    def setNeighborsList(self, newNeighborsList):
        self._neighborsList = newNeighborsList

    # Helper Methods
    def askSensorID(self):
        validInput = False
        while validInput is not True:
            try:
                # Get user input
                sensorID = input(
                    "_*__*__*__*__*__*__*__*__*__*_\nEnter the Sensor Id: ")
                # If user input is alphabetical
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
                # Get User input
                numNeighbors = int(input('Enter the number of neighbours: '))
            # If user input is not an integer
            except:
                print(
                    "This is an invalid entry for the neighbour's name and/or distance!")
            else:
                validInput = True
                return numNeighbors

    def getNeighborofSensor(self, sensorID):
        validInput = False
        while validInput is not True:
            # Get user input
            try:
                neighbor = input(
                    'Enter the neighbor for Sensor {0}: '.format(sensorID))
                # If user input is alphabetical and not the same as the sensor ID
                if neighbor.isalpha() and neighbor != self._id:
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
                # Get User input
                distance = int(
                    input('Enter the distance to {0}: '.format(sensorID)))
            # If user input is not an integer
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
                # Get user input
                oxygenLevel = int(input('Enter the Oxygen level in %: '))
            # If user input is not an integer
            except:
                print('This is an invalid entry for the oxygen level!')
            else:
                self.setOxygenLevel(oxygenLevel)
                validInput = True

    def getTemp(self):
        validInput = False
        while validInput is not True:
            try:
                # Get user input
                temp = float(input('Enter the temperature measurement: '))
            except:
                # If user input is not a float
                print('This is an invalid entry for the temperature!')
            else:
                self.setTemperature(temp)
                validInput = True

    @staticmethod
    def greetMessage(self):
        print("******************************************************************************\n\nWelcome to the company's IoT-Based Health System\nThese are sensors of {0} brand, and their Ad Hoc Mode is {1}\n\n******************************************************************************".format(
            self.BRAND_NAME, self.ADHOC_Mode))
