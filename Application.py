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

    # Accessor Methods
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

    # Mutator Methods
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

    # Helper Methods
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
                # Get user input
                numSensors = int(input("Enter the number of sensors: "))
            # If user input is not an integer
            except:
                print("This is an invalid entry for the number of sensors!")
            else:
                self.setNumSensors(numSensors)
                validInput = True

    def askSensorID(self, type):
        validInput = False
        while validInput is not True:
            try:
                # Get user input
                userInput = input('Enter the {0} sensor: '.format(type))
                # If user input is alphabetical
                if userInput.isalpha():
                    validInput = True
                    return userInput

                else:
                    raise TypeError
            except:
                print('This is an invalid entry for {0} sensor!'.format(type))

    def createSensors(self):
        count = 0  # Counting variable
        self.askNumSensors()  # Get number of sensors from user

        while count < self._numSensors:  # Loop block to iterate based on the value provided by user
            sensor = WirelessNetworks()  # Create sensor object
            sensor.askSensorID()  # Get sensor object ID

            countNeighbors = 0  # Counting variable
            numNeighbors = sensor.getNeighbors()  # Get neighbors for current sensor
            neighborsList = []

            while countNeighbors < numNeighbors:
                neighborID = sensor.getNeighborOfSensor(
                    sensor._id)  # Get neighbor ID
                neighborsList.append(neighborID)  # Add to list
                distToNeighbor = sensor.getDistance(
                    sensor._id)  # Get distance from sensor
                neighborsList.append(distToNeighbor)  # Add to list
                # Set value of list in sensor object
                sensor.setNeighborsList(neighborsList)
                countNeighbors += 1  # Iterate the count

            sensor.getOxygen()  # Get sensor Oxygen level
            sensor.getTemp()  # Get sensor Temperature level
            # Get value of list attribute in application object
            listSensors = self.getListSensors()
            listSensors.append(sensor)  # Add current sensor to list
            self.setListSensors(listSensors)  # Update list in object
            count += 1  # Iterate the count

    def convrtToDictionary(self, listSensors):
        dictSensors = self.getDictSensors()
        for sensor in listSensors:
            dictSensors[sensor._id] = sensor._neighborsList
            self.setDictSensors(dictSensors)

    def getSourceAndDestination(self):
        self.setSource(self.askSensorID('source'))
        self.setDestination(self.askSensorID('destination'))

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

    def findPath(self, dictSensors, source, destination, path):
        source = source
        destination = destination

        if len(path) == 0:
            self.addToPath(source)

        try:
            # Base Case
            if source == destination:
                return
            else:
                # Recursive loop
                nodeMaxDist = self.findNodeMaxDistance(
                    self.getPreviousSource(), source, dictSensors)  # Find node at max distance
                self.addToPath(nodeMaxDist)  # Add node to path
                # Remove element from dictionary
                self.setDictSensors(dictSensors.pop(source))
                self.setPrevSource(source)  # Update value of prevSource
                self.findPath(dictSensors, nodeMaxDist,
                              destination, self.getPath())  # Invoke recursive function with new source parameter
        except:
            # Alternative Case if no path can be found
            self.setPath([])
            print('The destination is not found')


App = Application()
WirelessNetworks.greetMessage(WirelessNetworks)
App.createSensors()
App.convrtToDictionary(App._listSensors)
App.getSourceAndDestination()
App.findPath(App._dictSensors, App._source, App._destination, App.getPath())
if App._path[-1] == App._destination:
    print('Path = {0}'.format(App._path))
