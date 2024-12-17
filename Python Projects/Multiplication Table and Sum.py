repeat = bool
num = 0

while repeat:  # loop for the system
    print("Please choose\n\t[1]Print Multiplication table based on user input \n\t"
          "[2]Compute the sum of all inputted numbers\n")
    table = input("Please choose: ")

    if table == "1":
        while True:  # loop for multiplication table
            try:  # to check if input value is valid
                num = int(input("Input number of multiplication: "))
            except ValueError:
                print("Invalid input")
                continue
            else:
                break
        for i in range(1, 11):  # calculation for multiplication table
            prod = num * i
            print(num, "*", i, "=", prod)

    elif table == "2":
        while True:  # loop for sum
            try:  # to check if input value is valid
                num = int(input("Enter how many inputs you want: "))
            except ValueError:
                print("Invalid input")
                continue
            else:
                suminput = 0.0  # variable float for sum

                for i in range(num):  # loop for input
                    while True:
                        try:  # to check if input value is valid
                            inputnum = float(input("Input number: "))
                            suminput += inputnum
                        except ValueError:
                            print("Invalid input")
                            continue
                        else:
                            break
                print("The sum of all inputted numbers are:", suminput)
                break

    else:
        print("Invalid input\n")

    while True:  # loop for choice if they want to continue
        print("Do you want to continue using the system?")
        userans = input("[Yes] [No]: ")

        if userans.lower() == "yes":
            break
        elif userans.lower() == "no":
            repeat = False
            print("Thank you!")
            break
        else:
            print("Invalid answer")