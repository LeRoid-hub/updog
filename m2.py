import os
import threading
from updog import Updog, HTTPGetBuilder, Logger, Server, Service, Notify, Email

os.environ["Enviroment"] = "dev"

server1 = Server("http://localhost", 8080)
me = Server("http://localhost", 8082)


service1 = HTTPGetBuilder(url="https://google.com", port=8080)
service1 = Service(service1)

notify = Email(465, "smtp.gmail.com", "janbar2001@gmail.com", "tntp mfds jirm lvon", ["janbar2001@gmail.com"])
notify = Notify(notify)
up2 = Updog([server1], False, [], Logger(), notify, me, 8082)
