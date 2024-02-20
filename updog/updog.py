from .logger import Logger
from .server import Server
from threading import Timer
from flask import Flask, request, jsonify
from urllib.request import urlopen, Request
import json

class Updog:
    """
    Updog class to manage the serverpool and services
    Provides the ability to detect if a server, database or another Instance is down
    Is structured as a master-slave system
    When the master is down, the next slave becomes the master
    When a slave is down, the master removes it from the serverpool
    If a service is down, the Admin can be notified via a custom sercive like Discord, Telegram, Email, etc.

    Attributes:
    - Serverpool (list): The list of servers in the serverpool queue
    - me (Server): The server the instance is running on
    - Master (bool): If the instance is the master
    - Services (list): The list of services to be checked
    - serviceTimer (Timer): The timer to check the services
    - slaveTimer (Timer): The timer to check the slaves
    - log (Logger): The logger object
    - app (Flask): The Flask app

    """
    Serverpool: list = []
    me: Server
    Master: bool = True
    Services: list = []
    serviceTimer: Timer
    slaveTimer: Timer
    log: Logger
    app = Flask(__name__)

    def __init__(self, Serverpool, Master, Services, Logger, port):
        """
        Constructor for the Updog class

        Parameters:
        - Serverpool (list): The list of servers in the serverpool queue
        - Master (bool): If the instance is the master
        - Services (list): The list of services to be checked
        - Logger (Logger): The logger object
        - port (int): The port the Flask app should run on

        Returns:
        - Updog: The Updog object
        """
        self.Serverpool = Serverpool
        self.Master = Master
        self.Services = Services
        self.log = Logger
        if not self.Master:
            self.anounceSlave()
        self.log.dev_log("Updog instance created")

        self.app.route('/updog', methods=['GET', 'POST'])(self.updog)
        self.app.route('/getServerpool', methods=['GET'])(self.get_Serverpool)
        self.app.route('/getServices', methods=['GET'])(self.get_Services)
        self.app.route('/newMaster', methods=['GET'])(self.new_master)
        self.app.run(port=port)

    def updog(self):
        """
        The updog route for the Flask app
        Used to add servers to the serverpool or to check if the server is up

        Methods:
            - POST: Adds a server to the serverpool
            - GET: Checks if the server is up
        """

        if request.method == 'POST':
            if request.json:
               data = request.json
               if data["type"] == "server":
                   server = Server(data["url"], data["port"])
                   self.addServer(server)
               else:
                   self.log.error_log("Invalid request")
                   return "Invalid request"
            else:
                self.log.error_log("Invalid request")
                return "Invalid request"

        elif request.method == 'GET':
            return "Status: OK"
        return "Updog"

    def get_Serverpool(self) -> jsonify:
        """
        The getServerpool route for the Flask app
        Used to get the serverpool
        """
        sp = []
        if self.me
            sp.append(self.me)

        sp.extend(self.Serverpool)

        return jsonify(Serverpool=[e.serialize() for e in self.Serverpool])

    def get_Services(self) -> jsonify:
        """
        The getServices route for the Flask app
        Used to get the services
        """
        return jsonify(Services=[e.serialize() for e in self.Services])

#TEST
    def new_master(self) -> jsonify:
        """
        Gets a new master
        """
        if request.json:
            data = request.json
            if data["type"] == "master":
                self.Master = False
                url  = data["url"] + ":" + data["port"]
                self.getservers(url)
                self.anounceSlave()
            else:
                self.log.error_log("Invalid request")
                return "status: 400"


    def anounceSlave(self) -> None:
        """
        Anounces a new slave to the master
        """
        self.getservers(None)
        server = self.Serverpool[0]

        port = server.getPort()
        url = server.getIP() + ":" + port + "/updog"
        req = Request(url)
        data = {"type": "server", "url": self.me.getIP(), "port": self.me.getPort()}

        req.add_header('Content-Type', 'application/json; charset=utf-8')
        jsondata = json.dumps(data)
        jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes

        req = Request(url, jsondataasbytes, method='POST')

        try:
            response = urlopen(req)
            if response.getcode() == 200:
                return
            else:
                self.log.error_log("Invalid response")
        except:
            self.log.error_log("Server not found")

        self.log.info_log("Slave anounced")


    def getservers(self, url):
        """
        Gets the serverpool from the master
        """
        if url == None:
            server = self.Serverpool[0]

            port = server.getPort()
            url = server.getIP() + ":" + port + "/getServerpool"


        req = Request(url)

        try:
            response = urlopen(req)
            if response.getcode() == 200:
                if response.json()["type"] == "serverpool":
#TODO
#TEST
                    self.Serverpool = response.json()["Serverpool"]
                else:
                    self.log.error_log("Invalid response")
            else:
                self.log.error_log("Invalid response")
        except:
            self.log.error_log("Server not found")
            return



#TEST
    def anounceMaster(self) -> None:
        """
        Anounces a new master to the slaves
        """
        for server in self.Serverpool:
            data = {"type": "master", "url": self.me.getIP(), "port": self.me.getPort()}

            jsondata = json.dumps(data)
            jsondataasbytes = jsondata.encode('utf-8')
            server.newMaster(jsondataasbytes)

#TODO
    def anounceServerpool(self) -> None:
        """
        Anounces the serverpool to the slaves
        """
        pass

    def addServer(self, server: Server) -> None:
        """
        Adds a server to the serverpool

        Parameters:
        - server (Server): The server to be added to the serverpool

        Example:
        ```
        updog.addServer(Server("http://localhost", "5000"))

        ```
        """
        self.Serverpool.append(server)
        self.orderServerpool()
        self.anounceServerpool()

    def removeServer(self, server) -> None:
        """
        Removes a server from the serverpool

        Parameters:
        - server (Server): The server to be removed from the serverpool
        """
        self.Serverpool.remove(server)

    def addService(self, service) -> None:
        """
        Adds a service to the services

        Parameters:
        - service (Service): The service to be added to the services

        Example:
        ```
        updog.addService(Service(PostgeSQLBuilder("http://localhost", "5000")))

        """
        if not callable(service.run()):
            return

        if service not in self.Services:
            self.Services.append(service)

    def removeService(self, service) -> None:
        """
        Removes a service from the services

        Parameters:
        - service (Service): The service to be removed from the services
        """
        if not callable(service):
            return

        if service in self.Services:
            self.Services.remove(service)

    def setMaster(self, master: bool) -> None:
        self.Master = master

    def getMaster(self) -> bool:
        """
        Returns:
        - bool: If the instance is the master
        """
        return self.Master

    def getServerpool(self) -> list:
        """
        Returns:
        - list: The serverpool
        """
        return self.Serverpool

    def getServices(self) -> list:
        """
        Returns:
        - list: The services
        """
        return self.Services

    def promoteSlave(self) -> None:
        """
        Promotes the next slave in line to master
        """
        if self.me.getRank() == 1:
            self.Master = True
            self.orderServerpool()
            self.anounceMaster()
        else:
            self.log.error_log("Cant promote slave, not next in line")

    def orderServerpool(self) -> None:
        """
        Orders the serverpool by rank
        """
        for i, server in enumerate(self.Serverpool):
           server.setRank(i)
           if server.getIP() == self.me.getIP() and server.getPort() == self.me.getPort():
               self.me.setRank(i)

    def demoteMaster(self) -> None:
        """
        Demotes the instance to slave
        """
        self.Master = False

    def runServices(self) -> None:
        """
        Runs the services
        """
        for service in self.Services:
            self.log.dev_log("Running service: " + service.__str__())
            res = service.run()
            self.log.dev_log("Service: " + service.__str__() + " returned: " + str(res))

    def checkSceduler(self, time: int) -> None:
        """
        The sceduler for the services

        Parameters:
        - time (int): The time between each check
        """
        self.serviceTimer = Timer(time, self.checkSceduler)
        self.runServices()

    def checkServerpool(self) -> None:
        """
        Checks the serverpool for down servers
        """
        notReachable = []
        masterDown = False

        for server in self.Serverpool:
           self.log.dev_log("Checking server: " + server)
#TEST
           if server.getIP() == self.me.getIP() and server.getPort() == self.me.getPort():
               continue

           res = server.checkServer()
#TEST
           if res == False:
               if server.getMaster() == True:
                   masterDown = True
               self.notify("Server down", server.getIP() + " war master= " + masterDown)
               notReachable.append(server)

        if len(notReachable) > 0:
            for server in notReachable:
                if masterDown and self.me.getRank() == 1:
                    self.promoteSlave()
                self.removeServer(server)
                self.orderServerpool()

    def notify(self, info: str, msg: str) -> None:
        """
        Notifies the master of an event

        Parameters:
        - info (str): The info of the event
        - msg (str): The message of the event
        """
        pass

    def slaveSceduler(self, time: int) -> None:
        """
        The sceduler for the slaves

        Parameters:
        - time (int): The time between each check in ms
        """
        self.slaveTimer = Timer(time, self.slaveSceduler)
        self.checkServerpool()

    def stopSlaveTimer(self) -> None:
        """
        Stops the slaveTimer
        """
        self.slaveTimer.cancel()

    def stopServiceTimer(self) -> None:
        """
        Stops the serviceTimer
        """
        self.serviceTimer.cancel()
