from urllib.request import urlopen, Request

class Server:
    """
    Server class to store server information

    Attributes:
    ip: str - IP address of the Server
    port: int - Port of the server
    master: bool - If the server is the master
    rank: int - The rank of the server

    """

    ip: str
    port: int = 80
    master: bool = False
    rank: int = 99

    def __init__(self,  ip: str, port: int):
        """
        Constructor for the Server class

        Parameters:
        - ip (str): The IP address of the server
        - port (int): The port of the server
        """

        self.ip = ip
        self.port = port

    def getIP(self) -> str:
        """
        Returns the IP address of the server

        Returns:
        - str: The IP address of the server
        """
        return self.ip

    def getPort(self) -> int:
        """
        Returns the port of the server

        Returns:
        - int: The port of the server
        """
        return self.port

    def setMaster(self, master: bool) -> None:
        """
        Sets the master attribute of the server
        And sets the rank to 0

        Parameters:
        - master (bool): The master attribute of the server
        """
        self.master = master
        self.rank = 0

    def getMaster(self) -> bool:
        """
        Returns the master attribute of the server

        Returns:
        - bool: The master attribute of the server
        """
        return self.master

    def setRank(self, rank: int) -> None:
        """
        Sets the rank of the server

        Parameters:
        - rank (int): The rank of the server
        """
        self.rank = rank

    def getRank(self) -> int:
        """
        Returns the rank of the server

        Returns:
        - int: The rank of the server
        """
        return self.rank

    def checkServer(self) -> bool:
        """
        Checks if the server is reachable

        Returns:
        - bool: If the server is reachable
        """
        try:
            res = urlopen(self.ip + ":" + str(self.port))
            if res.status == 200:
                return True
            return False
        except Exception as e:
            return False

    def newMaster(self, data: dict):
        """
        Gets notified that a new master has been elected
        """
        self.master = False
        try:
            req = Request('http://' + self.ip + ':' + str(self.port) + '/newMaster', data=data)
            res = urlopen(req)
            if res.status == 200:
                return True
            return False
        except Exception as e:
           return False

    def serialize(self) -> dict:
        """
        Serializes the Server object into a dictionary

        Returns:
        - dict: The serialized Server object
        """
        return {
            "ip": self.ip,
            "port": self.port,
            "master": self.master,
            "rank": self.rank
        }
