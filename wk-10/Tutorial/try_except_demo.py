guess = 0

while not(0 < guess < 6):

    try:
        guess = int(input("Enter an integer: "))
        if not(0 < guess < 6): raise Exception

    except ValueError:
        print("Requires an integer")

    except Exception:
        print("Requires an integer between 1 and 5")
