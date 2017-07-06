#My little take on demonstrating the Collatz conjecture
from Check import check

def IsInteger(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def Loop(n, YorN):
    steps = 0
    start = str(n)
    tipper = 0

    if not IsInteger(n):
        print("You didn't enter a number!")
        check()
    else:
        n = int(n)
        if n > 1:
            while n > 1:
                if n > tipper:
                    tipper = n
                if YorN:
                    print("Step", str(steps)+":", n)
                if n % 2 == 0:
                    steps +=1
                    n = n // 2
                else:
                    steps +=1
                    n = (3*n) + 1
            print(
                "It took", steps, "step(s) for the loop, starting at", 
                start+",", "to terminate. The loop climbed all the way to", tipper,
                "during the loop."
            )
        else:
            print("You need to enter a number greater than 1!")
            check()
            

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