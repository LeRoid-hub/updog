from updog import Updog, Email, Notify, Logger, Service, Server, HTTPGetBuilder

def main():
    logger = Logger()

    serverlist = []

    service1 = HTTPGetBuilder("http://www.google.com")
    service1 = Service(service1)
    servicelist = [service1]

    notify = Email(587, "smtp.gmail.com", "user", "pass", ["test@test.com"])
    notify = Notify(notify)

    me = Server("localhost", 8080)

    updog = Updog(serverlist, True, servicelist, logger, notify, me, 8080)

if __name__ == '__main__':
    main()
