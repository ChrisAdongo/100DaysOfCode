while True:  
    year = int(input("Enter the year you want to check.\n"))

    # if year % 400 == 0:
    #     print("Leap year.")
    # elif year % 100 == 0:
    #     print("Not a leap year..")
    # if year % 4 == 0:
    #     print("Leap year.")
    # else:
    #     print("Not a leap year.")

    # choice = input("Do you wish to continue. 'y' or 'n'?\n")
    # if choice != 'y':
    #      print("Goodbye!")
    #      break


    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Leap year.")
    else:
        print("Not a leap year.")

    choice = input("Do you wish to continue. 'y' or 'n'?\n")
    if choice != 'y':
        print("Goodbye!")
        break

