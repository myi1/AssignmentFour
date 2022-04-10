from WirelessNetworks import WirelessNetworks


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

    def createSensors(self):
        count = 0
        self.askNumSensors()

        while count <= self._numSensors:
            sensor = WirelessNetworks()
            sensor.askSensorID()

            countNeighbors = 0
            numNeighbors = self.getNeighbors()
            neighborsList = []

            while countNeighbors < numNeighbors:
                neighborID = sensor.getNeighborofSensor(sensor._id)
                neighborsList.append(neighborID)
                distToNeighbor = sensor.getDistance(sensor._id)
                neighborsList.append(distToNeighbor)
                sensor.setNeighborsList(neighborsList)
                countNeighbors += 1

            count += 1
            print(sensor._neighborsList)


App = Application()
App.createSensors()
