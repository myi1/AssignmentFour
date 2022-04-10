class Application:

    def __init__(self):
        self._listSensors = []

    def getListSensors(self):
        return self._listSensors

    def setListSensors(self, newListSensors):
        self._listSensors = newListSensors
