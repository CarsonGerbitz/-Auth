def SBURBHOST():
    import time
    import random
    print("Welcome to Skaia Net's SBURB Host Program")
    print("You are currently running version 4.1.3")
    def wait(waittime):
        time.sleep(waittime)
    def load(percent):
        while percent !=105:
            print(percent,"%")
            percent=percent+5;
            time.sleep(.5)
    load(0)
    print("SBURB is now fully loaded!")
    wait(.5)
    print("Pleas enter your SCREEN NAME")
    wait(.5)
    Name0 = input("YOUR NAME ")
    wait(.5)
    print("Hello " + Name0.upper() + " and welcome to SBURB!")
    wait(.5)
    print("Please enter the IP address of your client's machine ")
    wait(.5)
    clientIP = input("CLIENT'S IP ")
    wait(.5)
    print("Thanks!")
    wait(2)
    def hostping():
        import os
        clientname = clientIP
        response = os.system("ping -c 1 " + clientname)
        if response == 0:
            message = "Accecpt invite from " + name0 + "?"
            UDP_PORT = 27015
            print("CLIENT'S IP:", clientIP)
            print("SBURB SERVICE PORT:", UDP_PORT)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(bytes(MESSAGE, "utf-8"), (clientIP, UDP_PORT))
            print(clientname, 'CONNECTION MADE!')
        else:
            print(clientname, 'CONNECTION FAILED!')
    hostping()
SBURBHOST()
