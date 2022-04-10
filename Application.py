from WirelessNetworks import WirelessNetworks


class Application:

    def __init__(self):
        self._listSensors = []
        self._dictSensors = {}
        self._numSensors = 0
        self._source = ''
        self._destination = ''

    def getListSensors(self):
        return self._listSensors

    def getNumSensors(self):
        return self._numSensors

    def getDictSensors(self):
        return self._dictSensors

    def getSource(self):
        return self._source

    def getDestination(self):
        return self._destination

    def setListSensors(self, newListSensors):
        self._listSensors = newListSensors

    def setNumSensors(self, newNumSensors):
        self._numSensors = newNumSensors

    def setDictSensors(self, newDictSensors):
        self._dictSensors = newDictSensors

    def setSource(self, newSource):
        self._source = newSource

    def setDestination(self, newDestination):
        self._destination = newDestination

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

    def askSensorID(self, type):
        validInput = False
        while validInput is not True:
            try:
                userInput = input('Enter the {0} sensor: '.format(type))

                if userInput.isalpha():
                    validInput = True
                    return userInput

                else:
                    raise TypeError
            except:
                print('This is an invalid entry for {0} sensor!'.format(type))

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

    def getSourceAndDestination(self):
        self.setSource(self.askSensorID('source'))
        self.setDestination(self.askSensorID('destination'))

    def findPath(self, dictSensors, source, destination):
        source = source
        destination = destination
        path = []
        path.append(source)

        if source == destination:
            return path
        else:
            neighbors = dictSensors.get(source)
            if destination in neighbors:
                path.append(destination)
            else:
                self.findPath(dictSensors, neighbors[0], destination)

        print('Path = {0}'.format(path))


App = Application()
App.createSensors()
App.convrtToDictionary(App._listSensors)
App.getSourceAndDestination()
App.findPath(App._dictSensors, App._source, App._destination)
