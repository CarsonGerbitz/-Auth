import time
import datetime
def GHOTI():
    '''Starts the GHOTI game'''
    name = "null"
    today = datetime.date.today()
    def start():
        state = 1
        print("You stand in your room. Today's date is ", today)
        name = input("What is your name? ")
        print(name + "? Yeah, that sounds about right.")
        string = ". . ."
        for char in string:
            print(char, end='')
            time.sleep(.50)
        def room1():
            print(" ")
            print("So, " + name + " what do we do now?")
            def R1A1():
                action = input('Enter Action ')
                if action == 'help' or action == '?':
                    print("Look, Sleep, say")
                    R1A1()
                if action == "look":
                    print("This is your room. There is a bed, a desk with your computer on it, and clothes all over the floor.")
                    print("But you should really know this by now. Seeing as how this is your room.")
                    print("Now that you have once again seen your own room. What do you choose to do?")
                    def R1A2():
                        action = input('Enter Action')
                        if action == 'check':
                            check = input('What do you want to check? ')
                            if check == 'bed':
                                print("You see a blue sheet with a red blanket and 2 green pillows.")
                                print("Your bed is a mess")
                                print("Will you clean it?")
                                answer = input("Y/N? ")
                                if answer == 'y':
                                    print("You cleaned your bed.")
                                    print("Good job")
                                    R1A2()
                                if answer == 'n':
                                    print("Wow nice hygene skills buddy")
                                    R1A2()
                                if answer == '':
                                    print("Fine, just ignore me.")
                                    R1A2()
                            if check == 'desk' or check == 'computer':
                                print("You look at you computer screen and see that someone was trying to contact you.")
                                print("It was one of your good friends.")
                                print("What is you friend's name?")
                                friend1Name = input("Enter the name of your fiend ")
                                def R1A3():
                                    print("I am a placeholder")
                                R1A3()
                            if check == 'floor':
                                print("You can walk on that.")
                            if check == 'help':
                                print("Desk, Floor, Bed")
                        if action == 'say':
                            print("What's that now?")
                            talk = input("What do you say? ")
                            print("Wow that statement holds a vast amount of pertainance to the current situation.")
                        if action == 'help':
                            print("Check, Sleep, Say")
                            R1A2()
                        if action == 'sleep':
                            print("No! You are banned from going back to bed!")
                            R1A2()
                        else:
                            R1A2()
                    time.sleep(.5)
                    R1A2()
                if action == 'say':
                    print("What's that?")
                    talk = input("What do you say? ")
                    if talk == 'Deus Vult' or talk == 'deus vult':
                    	print("WE SHALL TAKE JERUSALUM COMRADE!")
                    	R1A1()
                    else:
                    	print("Wow that statement holds a vast amount of pertainance to the current situation.")
                    	R1A1()
                if action == 'sleep':
                    print("Now is not the time for sleeping!")
                    R1A1()
                else:
                    R1A1()
            R1A1()
        room1()
    start()
GHOTI()
