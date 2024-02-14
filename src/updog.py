from logger import Logger
from threading import Timer

class Updog:
    Serverpool: list = []
    ClusterMaster: str = ""
    Master: bool = True
    Services: list = []
    serviceTimer: Timer
    slaveTimer: Timer
    log: Logger

    def __init__(self, Serverpool, Master, Services, Logger) -> None:
        self.Serverpool = Serverpool
        self.Master = Master
        self.Services = Services
        self.log = Logger
        self.log.dev_log("Updog instance created")


    def addServer(self, server: str) -> None:
        self.Serverpool.append(server)

    def removeServer(self, server: str) -> None:
        self.Serverpool.remove(server)

    def addService(self, service) -> None:
        if not callable(service):
            return

        if service not in self.Services:
            self.Services.append(service)

    def removeService(self, service) -> None:
        if not callable(service):
            return

        if service in self.Services:
            self.Services.remove(service)

    def setMaster(self, master: bool) -> None:
        self.Master = master

    def getMaster(self) -> bool:
        return self.Master

    def getServerpool(self) -> list:
        return self.Serverpool

    def getServices(self) -> list:
        return self.Services

    def promoteSlave(self) -> None:
        self.Master = True

    def demoteMaster(self) -> None:
        self.Master = False

    def runServices(self) -> None:
        for service in self.Services:
            service()

    def checkSceduler(self, time: int) -> None:
        self.serviceTimer = Timer(time, self.checkSceduler)
        self.runServices()

    def checkServerpool(self) -> None:
        for server in self.Serverpool:
           self.log.dev_log("Checking server: " + server)

    def slaveSceduler(self, time: int) -> None:
        self.slaveTimer = Timer(time, self.slaveSceduler)
