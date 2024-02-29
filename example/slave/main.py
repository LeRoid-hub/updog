from updog import Updog, Email, Notify, Logger, Service, Server, HTTPGetBuilder

def main():
    logger = Logger()

    server1 = Server("localhost", 8080)
    serverlist = []

    notify = Email(587, "smtp.gmail.com", "user", "pass", ["test@test.com"])
    notify = Notify(notify)

    me = Server("localhost", 8080)

    updog = Updog(serverlist, False, [], logger, notify, me, 8081)

if __name__ == '__main__':
    main()
