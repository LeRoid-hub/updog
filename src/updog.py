from logger import Logger
from threading import Timer
from server import Server
from flask import Flask

class Updog:
    Serverpool: list = []
    me: Server
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
        if not self.Master:
            self.anounceSlave()
        self.log.dev_log("Updog instance created")

    def anounceSlave(self) -> None:
        self.log.info_log("Slave anounced")

    def anounceMaster(self) -> None:
        pass

    def addServer(self, server: str) -> None:
        self.Serverpool.append(server)

    def removeServer(self, server) -> None:
        self.Serverpool.remove(server)

    def addService(self, service) -> None:
        if not callable(service.run()):
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
        if self.me.getRank() == 1:
            self.Master = True
            self.orderServerpool()
            self.anounceMaster()
        self.log.error_log("Cant promote slave, not next in line")

    def orderServerpool(self) -> None:
        for i, server in enumerate(self.Serverpool):
           server.setRank(i)

    def demoteMaster(self) -> None:
        self.Master = False

    def runServices(self) -> None:
        for service in self.Services:
            self.log.dev_log("Running service: " + service.__str__())
            res = service.run()
            self.log.dev_log("Service: " + service.__str__() + " returned: " + str(res))

    def checkSceduler(self, time: int) -> None:
        self.serviceTimer = Timer(time, self.checkSceduler)
        self.runServices()

    def checkServerpool(self) -> None:
        for server in self.Serverpool:
           self.log.dev_log("Checking server: " + server)
           res = server.checkServer()
           if res == False:
               self.notify("Server down", server.getIP() + " war master= " + server.getMaster())
               self.removeServer(server)
               self.orderServerpool()
               if server.getMaster() == True:
                   self.promoteSlave()
                   server.setMaster(False)

#TODO
    def notify(self, info: str, msg: str) -> None:
        pass

    def slaveSceduler(self, time: int) -> None:
        self.slaveTimer = Timer(time, self.slaveSceduler)
