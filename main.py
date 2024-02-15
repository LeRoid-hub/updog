import os
from updog import Updog, HTTPGetBuilder, Logger, Server

os.environ["Enviroment"] = "dev"

server1 = Server("http://localhost", 8080)

service1 = HTTPGetBuilder("http://google.com", 8080)


up = Updog([server1],True,[service1],Logger(),8456)
print(up.getServices())

# up2 = Updog([],False,[service1],Logger(),8457)
