from WirelessNetworks import WirelessNetworks


class Application:

    def __init__(self):
        self._listSensors = []
        self._dictSensors = {}
        self._numSensors = 0

    def getListSensors(self):
        return self._listSensors

    def getNumSensors(self):
        return self._numSensors

    def getDictSensors(self):
        return self._dictSensors

    def setListSensors(self, newListSensors):
        self._listSensors = newListSensors

    def setNumSensors(self, newNumSensors):
        self._numSensors = newNumSensors

    def setDictSensors(self, newDictSensors):
        self._dictSensors = newDictSensors

    def askNumSensors(self):
        validInput = False
        while validInput is not True:
            try:
                numSensors = int(input("Enter the number of sensors: "))
            except:
                print("This is an invalid entry for the number of sensors!")
            else:
                self.setNumSensors(numSensors)
                validInput = True

    def createSensors(self):
        count = 0
        self.askNumSensors()

        while count < self._numSensors:
            sensor = WirelessNetworks()
            sensor.askSensorID()

            countNeighbors = 0
            numNeighbors = sensor.getNeighbors()
            neighborsList = []

            while countNeighbors < numNeighbors:
                neighborID = sensor.getNeighborofSensor(sensor._id)
                neighborsList.append(neighborID)
                distToNeighbor = sensor.getDistance(sensor._id)
                neighborsList.append(distToNeighbor)
                sensor.setNeighborsList(neighborsList)
                countNeighbors += 1

            sensor.getOxygen()
            sensor.getTemp()
            listSensors = self.getListSensors()
            listSensors.append(sensor)
            self.setListSensors(listSensors)
            count += 1

    def convrtToDictionary(self, listSensors):
        dictSensors = self.getDictSensors()
        for sensor in listSensors:
            dictSensors[sensor._id] = sensor._neighborsList
            self.setDictSensors(dictSensors)


App = Application()
App.createSensors()
App.convrtToDictionary(App._listSensors)
print(App.getDictSensors())
