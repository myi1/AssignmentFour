from WirelessNetworks import WirelessNetworks


class Application:

    def __init__(self):
        self._listSensors = []
        self._dictSensors = {}
        self._numSensors = 0
        self._source = ''
        self._destination = ''
        self._path = []
        self._prevSource = ''

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

    def getPath(self):
        return self._path

    def getPreviousSource(self):
        return self._prevSource

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

    def setPath(self, newPath):
        self._path = newPath

    def setPrevSource(self, newPrevSource):
        self._prevSource = newPrevSource

    def addToPath(self, node):
        path = self.getPath()
        path.append(node)
        self.setPath(path)

    def removeLastNodeFromPath(self):
        path = self.getPath()
        path.pop()
        self.setPath(path)

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

    def findPath(self, dictSensors, source, destination, path):
        source = source
        destination = destination

        if len(path) == 0:
            self.addToPath(source)

        try:
            if source == destination:
                return
            else:

                nodeMaxDist = self.findNodeMaxDistance(
                    self.getPreviousSource(), source, dictSensors)
                self.addToPath(nodeMaxDist)
                self.setDictSensors(dictSensors.pop(source))
                self.setPrevSource(source)
                self.findPath(dictSensors, nodeMaxDist,
                              destination, self.getPath())
        except:
            self.setPath([])
            print('The destination is not found')

    def findNodeMaxDistance(self, prevSource, key, dict):
        list = dict[key]
        if prevSource != "":
            indexPrev = list.index(prevSource)
            list.pop(indexPrev + 1)
            list.pop(indexPrev)

        changedList = list[-1::-2]
        changedList.reverse()

        maxValue = max(changedList)
        index = list.index(maxValue)
        maxDistanceNode = list[index-1]

        return maxDistanceNode


App = Application()
App.createSensors()
App.convrtToDictionary(App._listSensors)
App.getSourceAndDestination()
App.findPath(App._dictSensors, App._source, App._destination, App.getPath())
if App._path[-1] == App._destination:
    print('Path = {0}'.format(App._path))
