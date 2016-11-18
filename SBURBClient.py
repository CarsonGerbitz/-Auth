def SBURBCLIENT():
    import time
    import random
    print("Welcome to Skaia Net's SBURB Client Program")
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
    print("Please enter the IP address of your host's machine ")
    wait(.5)
    hostIP = input("HOST'S IP ")
    wait(.5)
    print("Thanks!")
    wait(2)
    def hostping():
        import os
        hostname = hostIP
        response = os.system("ping -c 1 " + hostname)
        if response == 0:
            print(hostname, 'CONNECTION MADE!')
        else:
            print(hostname, 'CONNECTION FAILED!')
    hostping()
SBURBCLIENT()
