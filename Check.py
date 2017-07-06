#Jim Vargas
#A useful check thing that lets users decide if they want to continue or 
#quit if they mess up on inputs

#REQUIRES a function called main() in order to work!!!

def check():
    print("Do you want to continue?")
    thing = input("Y or N?"+'\n'+">>> ")
    if (thing == "Y") or (thing == "y"):
        main()
    elif (thing == "N") or (thing == "n"):
        print("Quitting...")
        exit()
    elif len(thing) == 0:
        print("You didn't enter anything.")
        print("Quitting...")
        exit()
    elif len(thing) > 1:
        print("The program needs a one letter anser.", '\n')
        check()
    else:
        print("You entered something invalid.")
        print("Quitting...")
    exit()