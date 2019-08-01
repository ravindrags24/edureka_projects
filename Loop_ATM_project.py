#  Nested Loop example to simulate a bank ATM using Python 3.

print( "Welcome to your nearby banking ATM")

#  Variables for account balance, ATM pin retries &  If Yes for previous menu

number = 15000
chances = 3
restart = ('Y')

#  Loop starts from here.

while chances >= 0:
    pin = int(input("Please enter you 4 Digit Pin number: "))
    if pin == (3434):
        while restart not in ('n','NO','no','N'):

            #  We are providing options for bank customers

            option = int(input("Here are your options: \n  1. Check Balance \n  2. Make a withdrawal \n  3. Pay in \n  4. Return card \n"))

            if option == 1:
                print("Your available balance", number)
                restart = input('Would you like to go back Main manu?  ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break

            elif option == 2:
                withdraw = int (input("Entry the amount: "))
                number = number - withdraw

                if number > 0 and withdraw > 0:
                    print("Your total available balance: ", number)
                elif number < 0:
                    print("Entered amount is not correct")
                    print("Your total amount available", number + withdraw )
                elif withdraw < 0:
                    print("Entered amount is available ! Choose again!")
                    print("Your total amount available", number + withdraw)

                    restart = input('Would you like to go back Main manu? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break

            elif option == 3:
                deposit = int (input("Enter the amount you want to pay in ?  "))
                number = number + deposit

                if number > 0 and deposit > 0:
                    print("Your total amount:" , number)
                elif number < 0:
                    print("Entered amount is wrong ! Choose again!")
                    print("Your total amount available", number + deposit)
                elif deposit < 0:
                    print("Entered amount is wrong ! Choose again!")
                    print("Your total amount available", number + deposit)

                    restart = input('Would you like to go back Main manu? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break

            elif option == 4:
                print('Please wait while your card is Returned...\n')
                print('Thank you for your service')
                break

            else:
                print('Please enter a correct number. \n')
                restart = ('y')

#   We are retrying 3 times for correct pin number if failed exit from program with appropriate message.

    elif pin != ('3434'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            break





