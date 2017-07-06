#My little take on demonstrating the Collatz conjecture

def IsInteger(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def Loop(n, YorN):
    steps = 0
    if not IsInteger(n):
        print("You didn't enter a number!")
        check()
    else:
        n = int(n)
        if n > 1:
            while n > 1:
                if YorN:
                    print("Step", str(steps)+":", n)
                if n % 2 == 0:
                    steps +=1
                    n = n // 2
                else:
                    steps +=1
                    n = (3*n) + 1
            print("It took", steps, "step(s) for the loop to terminate.")
        else:
            print("You need to enter a number greater than 1!")
            check()


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


def main():
    n = input("Enter an integer greater than 1"+'\n'+">>> ")

    print("Would you like the prgram to print the steps as it goes along?")
    Psteps = input("Y or N?"+'\n'+">>> ")

    if (Psteps == "Y") or (Psteps == "y"):
        Psteps = True
    else:
        Psteps = False

    
    Loop(n, Psteps)


if __name__ == '__main__':
    main()