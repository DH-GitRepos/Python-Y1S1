def log_error(txt):
    with open('error.txt', 'a') as f:
        print(txt, file=f)


guess = 0

while not(0 < guess < 6):
    try:
        guess = int(input("Enter an integer: "))
        if not(0 < guess < 6):
            raise Exception("Integer was out of range: " + str(guess))

    except ValueError as err:
        print("Entry must be an integer.", end=' ')
        log_error(err)

    except Exception as err:
        print("Entry must be from 1 to 5 inclusive.", end=' ')
        log_error(err)
