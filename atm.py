balance = 10000
pin ="1234"
entered_pin = input("enter PIN: ")
if entered_pin == pin:
    while True:
        print("\n1.check balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")
        choice = input("enter choice: ")
        if choice == "1":
            print("Balance:",balance)
        elif choice =="2":
            amount = int(input("enter amount: "))
            balance= balance+ amount
            print("amount deposited")
        elif choice == "3":
            amount = int(input("enter amount: "))
            if amount <= balance:
                balance = balance-amount
                print("amount withdrawn")
            else:
                print("Insufficient balance")
        elif choice == "4":
            break
        else:
            print("Invalid choice")
else:
    print("Wrong PIN")
 
