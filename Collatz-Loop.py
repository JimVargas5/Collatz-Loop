#My little take on demonstrating the Collatz conjecture

def IsInteger(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def Loop(n):
    steps = 0
    if not IsInteger(n):
        print("You didn't enter a number!")
        main()
    else:
        n = int(n)
        if n > 1:
            while n > 1:
                if n % 2 == 0:
                    steps +=1
                    n = n / 2
                else:
                    steps +=1
                    n = (3*n) + 1
            print("It took", steps, "step(s) for the loop to terminate.")
        else:
            print("You need to enter a number greater than 1!")
            main()


def main():
    n = input("Enter an integer greater than 1"+'\n'+">>> ")
    Loop(n)


if __name__ == '__main__':
    main()